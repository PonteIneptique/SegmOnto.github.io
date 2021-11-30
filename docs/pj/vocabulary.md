# Vocabulary

SegmOnto is not the first attempt to offer a description of a page. Because of the nature of the task, two different academic traditions have offered vocabularies that serve as a base:

- Computer vision, especially via the PAGE XML scheme, proposes a limited system adapted to the needs of computer scientists.
- Codicology, whose purpose precisely is the description of the old documents, offers a much more precise vocabulary to answer the needs of philologists.

On the one hand, codicological vocabularies do not take into account the requirements of computer-based solutions (such as a system of private zones or the articulation of types and subtypes) and usually does not address contemporary cases. On the other hand, the solution offered by computer scientists is too poor and is incapable to offer a satisfactory description of a page taken from an historical document. For all these reasons, SegmOnto offers a middle way, in between these two.

## Page

PAGE XML (cf. _infra_) offers a simple, short and generalist scheme to describe the page, with only fourteen categories:

- `TextRegionType`. Pure text is represented as a text region. This includes drop capitals, but practically ornate text may be considered as a graphic.
- `ImageRegionType`. An image is considered to be more intricate and complex than a graphic. These can be photos or drawings.
- `LineDrawingRegionType`. A line drawing is a single colour illustration without solid areas.
- `GraphicRegionType`. Regions containing simple graphics, such as a company logo, should be marked as graphic regions.
- `TableRegionType`. Tabular data in any form is represented with a table region. Rows and columns may or may not have separator lines; these lines are not separator regions.
- `ChartRegionType`. Regions containing charts or graphs of any type, should be marked as chart regions.
- `SeparatorRegionType`. Separators are lines that lie between columns and paragraphs and can be used to logically separate different articles from each other.
- `MathsRegionType`. Regions containing equations and mathematical symbols should be marked as maths regions.
- `ChemRegionType`. Regions containing chemical formulas.
- `MusicRegionType`. Regions containing musical notations.
- `AdvertRegionType`. Regions containing advertisements.
- `NoiseRegionType`. Noise regions are regions where no real data lies, only false data created by artifacts on the document or scanner noise.
- `UnknownRegionType`. To be used if the region type cannot be ascertained.
- `CustomRegionType`. Regions containing content that is not covered by the default types (text, graphic, image, line drawing, chart, table, separator, maths, map, music, chem, advert, noise, unknown).

## _Codicologia_

Other vocabularies, designed by philologist specialised in codicology, offer an interesting alternative to those designed by computer scientists. Under the supervision of the IRHT in Paris, several glossaries have been gathered in an online application called Codicologia. It offers an extensive vocabulary in French, most of the time with English, German, Italian, Spanish and Arabic translations, with precise definitions adapted to the need of academics specialised in the humanities. Thanks to Georg Vogeler, a digital version is also available as a SKOS model, perfectly suited for digital purposes.

## Towards a middle way

Because PAGE offers too general a description, it has been been decided not to expand it, but rather to reduce to the maximum the _Codicologia_ glossary. The reduction process has followed a simple criterion: unlike other vocabularies (like the TEI), _SegmOnto_ focuses on the form rather than the content/meaning. For instance, it uses `GraphicZone`, without making the difference between an illustration (which carries a semantic load) and an ornamentation (which is purely decorative).

Because of this reduction process, elements and definitions may differ:

- `GraphicZone` does not exist in _Codicologia_: it aggregates `Illustration` and `Ornamentation` of _Codicologia_. On top of these two, it aggregates a third type: figures (for schemas found in scientific works, for instance).
- `QuireMarksZone includes the _Signature_ (quire numbers) and the _Catchword_, which are two different elements in _Codicologia_.
