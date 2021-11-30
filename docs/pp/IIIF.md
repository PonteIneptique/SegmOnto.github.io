# IIIF

The International Image Interoperability Framework (IIIF) defines several application programming interfaces that provide a standardised method of describing and delivering images over the web, as well as "presentation based metadata" (that is, structural metadata) about structured sequences of images. It uses IIIF manifests, encoded in JSON.

The Manifest resource typically represents a single object and any intellectual work or works embodied within that object. In particular it includes descriptive, rights and linking information for the object. The Manifest embeds the Canvases that should be rendered as views of the object and contains sufficient information for the client to initialize itself and begin to display something quickly to the user.

A basic IIIF would be as follows:

```json
{
    "@context": "http://iiif.io/api/presentation/2/context.json",
    "@id": "https://www.segmonto.ch/metadata/iiif/ADD_ID_DOC/manifest.json",
    "@type": "sc:Manifest",
    "label": "ADD_FULL_REFERCENCE",
    "metadata": [
        {
            "label": "Location",
            "value": "ADD_LOCATION"
        },
        {
            "label": "Collection Name",
            "value": "ADD_COLLECTION"
        },
        {
            "label": "Shelfmark",
            "value": "ADD_SHELFMARK"
        },
        {
            "label": "Document Type",
            "value": "ADD_TYPE"
        },
        {
            "label": "Title (English)",
            "value": "ADD_TITLE"
        },
        {
            "label": "Text Language",
            "value": "ADD_LANGUAGE"
        }
    ],
    "description": [
        {
            "@value": "ADD_A_SUMMARY",
            "@language": "en"
        }
    ],
    "license": "http://creativecommons.org/licenses/by-nc/4.0/",
    "attribution": "DH Portal, université de Genève",
    "sequences": [
        {
            "@id": "https://www.segmonto.ch/metadata/iiif/ADD_ID_DOC/sequence/Sequence-3423.json",
            "@type": "sc:Sequence",
            "label": [
                {
                    "@value": "Normal Sequence",
                    "@language": "en"
                }
            ],
            "canvases": [
                {
                    "@id": "https://www.segmonto.ch/metadata/iiif/ADD_ID_DOC/canvas/ADD_ID_PAGE.json",
                    "@type": "sc:Canvas",
                    "label": "1r",
                    "height": 8000,
                    "width": 6000,
                    "images": [
                        {
                            "@id": "https://www.segmonto.ch/metadata/iiif/ADD_ID_DOC/annotation/ADD_ID_PAGE.json",
                            "@type": "oa:Annotation",
                            "motivation": "sc:painting",
                            "on": "https://www.segmonto.ch/metadata/iiif/ADD_ID_DOC/canvas/ADD_ID_PAGE.json",
                            "resource": {
                                "@id": "https://www.segmonto.ch/loris/ADD_ID_LIBRARY/ADD_ID_DOC/ADD_ID_PAGE.jp2/full/full/0/default/jpg",
                                "@type": "dctypes:Image",
                                "format": "image/jpeg",
                                "height": 8000,
                                "width": 6000
                            }
                        }
                    ]
                }
            ]
        }
    ]
}
```
