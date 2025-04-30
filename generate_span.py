import arcpy
import statistics

class Toolbox:
    def __init__(self):
        self.label = "Span Generation Toolbox"
        self.alias = "spangenerator"
        self.tools = [GenerateSpansFromStructures]


class GenerateSpansFromStructures:
    def __init__(self):
        self.label = "Generate Spans from Circuit and Structures"
        self.description = "Generates span lines between ordered pole structures based on a selected circuit."

    def getParameterInfo(self):
        params = [
            arcpy.Parameter(
                displayName="Circuit Line (selected)",
                name="circuit_line",
                datatype="GPFeatureLayer",
                parameterType="Required",
                direction="Input"
            ),
            arcpy.Parameter(
                displayName="Structures Layer",
                name="structures_layer",
                datatype="GPFeatureLayer",
                parameterType="Required",
                direction="Input"
            ),
            arcpy.Parameter(
                displayName="Output Span Feature Class",
                name="output_fc",
                datatype="DEFeatureClass",
                parameterType="Required",
                direction="Output"
            ),
            arcpy.Parameter(
                displayName="Buffer Distance (feet)",
                name="buffer_distance",
                datatype="GPDouble",
                parameterType="Optional",
                direction="Input",
                defaultValue=50
            ),
            arcpy.Parameter(
                displayName="Span Tolerance Factor",
                name="span_tolerance_factor",
                datatype="GPDouble",
                parameterType="Optional",
                direction="Input",
                defaultValue=1.5
            )
        ]
        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        circuit_line = parameters[0].valueAsText
        structures_layer = parameters[1].valueAsText
        output_fc = parameters[2].valueAsText
        buffer_distance = parameters[3].value or 50
        span_tolerance_factor = parameters[4].value or 1.5

        arcpy.env.overwriteOutput = True

        if int(arcpy.management.GetCount(circuit_line)[0]) != 1:
            raise ValueError("Please select exactly one circuit line.")

        route_id_field = "OBJECTID"

        buffered = arcpy.analysis.Buffer(circuit_line, "in_memory/buffered", f"{buffer_distance} Feet")
        near_structures = arcpy.analysis.Intersect([buffered, structures_layer], "in_memory/near_structures")

        located_poles = "in_memory/located_poles"
        arcpy.lr.LocateFeaturesAlongRoutes(
            near_structures, circuit_line, route_id_field,
            f"{buffer_distance} Feet", located_poles,
            f"{route_id_field} POINT MEAS"
        )

        pole_list = []
        with arcpy.da.SearchCursor(located_poles, ["SHAPE@XY", "MEAS", "StructureID", "StructureType", "CircuitName"]) as cursor:
            for row in cursor:
                pole_list.append({
                    "xy": row[0],
                    "m": row[1],
                    "id": row[2],
                    "type": row[3],
                    "circuit": row[4]
                })

        pole_list = [p for p in pole_list if p["m"] is not None]
        pole_list.sort(key=lambda x: x["m"])

        if len(pole_list) < 2:
            raise ValueError("Not enough poles found to generate spans.")

        spans = []
        lengths = []
        for i in range(len(pole_list) - 1):
            p1, p2 = pole_list[i], pole_list[i + 1]
            length = ((p2["xy"][0] - p1["xy"][0])**2 + (p2["xy"][1] - p1["xy"][1])**2)**0.5
            lengths.append(length)
            spans.append({"from": p1, "to": p2, "length": length})

        median_len = statistics.median(lengths)
        tolerance = median_len * span_tolerance_factor

        sr = arcpy.Describe(circuit_line).spatialReference
        arcpy.management.CreateFeatureclass("in_memory", "spans", "POLYLINE", spatial_reference=sr)
        output_path = "in_memory/spans"
        arcpy.management.AddFields(output_path, [
            ["FromID", "TEXT"],
            ["ToID", "TEXT"],
            ["SpanLen", "DOUBLE"],
            ["Flags", "TEXT"]
        ])

        with arcpy.da.InsertCursor(output_path, ["SHAPE@", "FromID", "ToID", "SpanLen", "Flags"]) as ic:
            for s in spans:
                p1, p2 = s["from"]["xy"], s["to"]["xy"]
                poly = arcpy.Polyline(arcpy.Array([arcpy.Point(*p1), arcpy.Point(*p2)]), sr)
                flags = []
                if s["length"] > tolerance:
                    flags.append("LongSpan")
                if s["from"]["type"] != s["to"]["type"]:
                    flags.append("TypeMismatch")
                if s["from"]["circuit"] != s["to"]["circuit"]:
                    flags.append("CircuitMismatch")
                ic.insertRow([poly, s["from"]["id"], s["to"]["id"], s["length"], ";".join(flags)])

        arcpy.management.CopyFeatures(output_path, output_fc)
        arcpy.AddMessage(f"Generated {len(spans)} spans with flags written to {output_fc}.")

    def postExecute(self, parameters):
        return
