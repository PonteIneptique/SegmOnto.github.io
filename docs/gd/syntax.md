# Syntax

There are two classes of regions: **zones** (an area, _i.e._ a polygon, on the page) and **lines** (an area, plus a baseline).

Zones or lines can be caracterised by:

- a type (mandatory, controlled values)
- a subtype (optional, suggested open list of values)
- a number (optional)

using the following syntax:

```regex
Region(:subtype)?(#\d)?
```

_e.g._:

`MainZone`

can be completed the following way:

- `MainZone#1`
- `MainZone:column`
- `MainZone:column#1`
