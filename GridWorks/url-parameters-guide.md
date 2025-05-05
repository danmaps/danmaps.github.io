# GridScaper URL Parameters Guide

GridScaper supports several URL parameters that allow you to customize the simulation without modifying the code. This guide explains the available parameters and how to use them.

## Available Parameters

### Grid Dimensions
- `size-x`: Width of the grid in units
- `size-y`: Depth of the grid in units

### Pole Configuration
- `poles-distances`: Comma-separated list of distances along the Z-axis for poles
- `poles-heights`: Comma-separated list of heights for each pole
- `poles-elevations`: Comma-separated list of ground elevations at each pole

## Usage

Parameters are added to the URL after a question mark (`?`), with multiple parameters separated by an ampersand (`&`).

```
GridScaper.html?parameter1=value1&parameter2=value2
```

## Examples

### Example 1: Custom Grid Size

Create a 200×150 unit grid:

```
GridScaper.html?size-x=200&size-y=150
```

### Example 2: Basic Line Profile with Three Poles

Create a line with poles at z=0, z=20 and z=40, with varying heights and elevations:

```
GridScaper.html?poles-distances=0,20,40&poles-heights=10,15,12&poles-elevations=0,5,2
```

### Example 3: Valley Crossing

Create a simulation of a power line crossing a valley:

```
GridScaper.html?poles-distances=0,25,50&poles-heights=20,25,20&poles-elevations=10,0,10
```

### Example 4: Hill Crossing

Create a simulation of a power line crossing a hill:

```
GridScaper.html?poles-distances=0,25,50&poles-heights=25,15,25&poles-elevations=0,10,0
```

### Example 5: Combined Parameters

Customize both grid size and pole placement:

```
GridScaper.html?size-x=100&size-y=100&poles-distances=0,30,60,90&poles-heights=15,20,20,15&poles-elevations=0,5,5,0
```

## Important Notes

1. All three pole parameters (`poles-distances`, `poles-heights`, and `poles-elevations`) must be provided together and have the same number of values.

2. When pole parameters are provided, the grid width will automatically be set to 50 units unless explicitly specified with `size-x`.

3. Poles are positioned along the Z-axis (lengthwise along the terrain strip) rather than across it.

4. Distances are in arbitrary units, heights are in feet, and elevations are relative to zero.

5. The terrain will automatically adjust to match the provided elevations, creating a smooth sloped surface through all pole locations.

6. You can still interact with the simulation after it's initialized with URL parameters - add poles, adjust tension, etc.
