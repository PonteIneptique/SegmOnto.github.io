# ALTO

The ALTO (Analyzed Layout and Text Object) and PAGE (Page Analysis and Ground truth Elements) are two open XML schemas, developed for the description of textual and layout information of page scans. The objective is to describe both in order to reconstruct the original appearance of the source document, based on the digitised information.

ALTO encoding is extremely simple. On top of metadata, it is structured as a tree with the following elements:

- `<Page> for the page
- `<PrintSpace>` for the part of the aforementioned `<Page>` with printed information
- `<TextBlock>` for different zones within the `<PrintSpace>`
- `<TextLine>` for each line in a given `<TextBlock>`
- `<String>` for the text contained in the `<TextLine>`.

```xml
<alto>
 <Description>
  <MeasurementUnit/>
  <sourceImageInformation/>
  <Processing/>
 </Description>
 <Styles>
  <TextStyle FONTSIZE="10.0"/>
  <ParagraphStyle ALIGN="Left"/>
 </Styles>
 <Layout>
  <Page ID="P1" WIDTH="123" HEIGHT="456">
   <PrintSpace WIDTH="123" HEIGHT="456"
    HPOS="789" VPOS="123">
    <TextBlock ID="ID_tb1" TAGREFS="BT1"
     WIDTH="123" HEIGHT="456" HPOS="789" VPOS="123">
     <Shape>
      <Polygon POINTS="123 456 789 123 456 789"/>
     </Shape>
     <TextLine ID="ID_tb1" TAGREFS="BT1"
      BASELINE="123 456 789" WIDTH="123" HEIGHT="456" HPOS="789"
      VPOS="123">
      <Shape>
       <Polygon POINTS="123 456 789 123 456 789"/>
      </Shape>
      <String CONTENT="Un" WIDTH="123"
       HEIGHT="456" HPOS="789" VPOS="123"/>
     </TextLine>
    </TextBlock>
   </PrintSpace>
  </Page>
 </Layout>
</alto>
```

PAGE XML is an alternative to ALTO, currently not supported by our pipeline. It follows a similar structure than ALTO

- `<TextRegion>` for the different zones
- `<Baseline> for the posting line
- `<Word>` for word-level tokens
- `<Coords>` for the coordinates of the given zone or line.
- `<TextEquiv>` for the transcription

```xml
<PcGts>
 <Metadata>
  <Creator>John Doe</Creator>
  <Created>2021-11-24T18:41:57.801+02:00</Created>
 </Metadata>
 <page>
  <TextRegion type="paragraph" id="r_1">
   <Coords points="1474,486 3684,486 3684,900…">
    <TextLine id="l_1">
     <Coords points="1475,487 3683,487 3683,635…">
      <Baseline points="1475,635 1587,635 2061…">
       <Word id="w1">
        <Coords points="1475,497 1587,497 1587…"/>
        <TextEquiv>
         <Unicode>Un</Unicode>
        </TextEquiv>
       </Word>
       <Word id="w2">
        <Coords points="1935,497 2061,497 2061,619…"/>
        <TextEquiv>
         <Unicode>exemple</Unicode>
        </TextEquiv>
       </Word>
       <TextEquiv>
        <Unicode>Un exemple</Unicode>
       </TextEquiv>
      </Baseline>
     </Coords>
    </TextLine>
   </Coords>
  </TextRegion>
 </page>
</PcGts>
```


