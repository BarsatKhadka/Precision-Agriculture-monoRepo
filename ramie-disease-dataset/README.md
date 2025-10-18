# Ramie Disease Dataset

This repository contains a comprehensive dataset of diseases and pests affecting ramie (Boehmeria nivea), a flowering plant in the nettle family Urticaceae, known for its strong bast fibers used in fabric production.

## Dataset Overview

The dataset contains information about 19 different diseases and pests affecting ramie plants, including:
- 11 diseases (fungal, viral, and complex diseases)
- 8 pest infestations (insects and other organisms)

## Data Format

The data is available in two formats:
1. CSV file (`data/ramie_diseases.csv`)
2. SQL insert statements (`data/ramie_diseases.sql`)

### Data Structure

Each entry in the dataset contains the following fields:

| Field | Description |
|-------|-------------|
| disease | Name of the disease or pest infestation |
| causal_organism | Scientific name of the organism causing the disease/infestation |
| time_of_occurence | Seasonal or temporal pattern of the disease/pest |
| incidence | Severity or impact on yield |
| place_of_occurence | Geographic location where the disease/pest was documented |
| reference | Academic reference for the disease/pest documentation |
| img_file | Path to the associated image file |

## Disease Categories

### Fungal Diseases
1. Brown root rot (Pythium vexans)
2. Cercospora leaf spot (Cercospora boehmeria)
3. Anthracnose leaf spot (Colletotrichum gloeosporioides)
4. Collar rot (Sclerotium rolfsii)
5. Angular Leaf Spot (Pseudocercospora boehmeriae)
6. Black leaf spot (Alternaria alternata)
7. Curvularia leaf blight (Curvularia eragrostidis)

### Viral Diseases
1. Yellow Mosaic (Viral disease)

### Complex Diseases
1. Wilt (Complex disease)

### Pest Infestations
1. Ramie moth (Cocytodes coerulea Guenée)
2. Indian red admiral caterpillar (Vanessa indica Herbst)
3. Leaf folder/Leaf roller (Spodoptera sp.)
4. Epilachna beetle (Cheilomenes sexmaculata/Micraspis discolor)
5. Hairy caterpillar (Spilosoma obliqua)
6. Leaf beetle (Pachnephorous bretinghami Baly)
7. Termite (Microtermes sp.)
8. White grub (Lepidiota sp.)
9. Black fungus beetle (Alphitobius piceus Olivier)

## Geographic Distribution

The dataset includes observations from multiple locations:
- Hunan Province, China
- Hubei Province, China
- Ramie Research Station, Sorbhog, Assam, India
- Various locations in Java, Indonesia (Bogor, Lembang, Tasikmalaya, Garut, and Malang)

## Severity Range

Disease/pest impact varies significantly:
- Yield loss ranges from 2-5% to over 40%
- Some diseases affect specific growth stages
- Temporal patterns vary from seasonal to year-round occurrence

## Image Data

The dataset includes corresponding images for each disease/pest, stored in the `/images` directory. Images are available in various formats (jpg, jpeg, png) and show the visual symptoms or damage caused by each disease/pest.


## Data Sources

The dataset compiles research from multiple academic sources, primarily from:
1. CRIJAF, ICAR (Indian Council of Agricultural Research)
2. Various Chinese agricultural research institutions
3. Indonesian agricultural research organizations

## References

For detailed references for each disease/pest, please refer to the individual entries in the dataset files.

## Contributing

If you have additional data or corrections, please submit a pull request with:
- Clear description of changes
- Academic references for new data
- High-quality images (if applicable)
