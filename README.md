# EIP Stats

url: <https://eip.epitech.eu/>

pypi: <https://pypi.org/project/eiptek3api/>

> [!TIP]
> If you want a browser user interface, use [this](https://github.com/Guilhemvnt/super-duper-data) instead.

## Usage

1. Login to eip website.
2. Open the console and write: `console.log(localStorage["token"])`
3. Install `eiptek3api` package `pipx install eiptek3api`
5. Run `eiptek3api`

## Doc

### Help

```bash
eiptek3api --help
```

```txt
usage: eiptek3api [-h] [--year YEAR] [--include-rejected] [--dump-projects] [filters ...]

CLI for https://eip-tek3.epitest.eu stats.

positional arguments:
  filters             `field__eq=value` or `path__to__field__eq=value` or `field__contains=value`

options:
  -h, --help          show this help message and exit
  --year YEAR         2023 for Promo 2026 | 2024 for Promo 2027 | i.e.: the date of the third year for your promo
  --include-rejected  Include project with status 'rejected'
  --dump-projects     Write all projects details to a dump_projects.json file

Made with 💜 by Saverio976
```

### Examples

#### Stats for all projects without filters

```bash
eiptek3api
```

#### Include rejected project

```bash
eiptek3api --include-rejected
```

#### Dump a file with all projects details

```bash
eiptek3api --dump-projects
```

#### Stats for projects with tags containing 'Machine Learning'

```bash
eiptek3api --year 2023 "tags__label__eq=Machine Learning"
```

#### Stats for projects in 'Paris' and tags containing 'Machine Learning'

```bash
eiptek3api --year 2023 "tags__label__eq=Machine Learning" "owner_city__name__eq=Paris"
```

#### Stats for projects containing 'eco' in the description

```bash
eiptek3api --year 2023 "description__contains=eco"
```

#### Stats for project that have a member with te firstname 'Xavier'

```bash
eiptek3api --year 2023 "members__firstname__eq=Xavier"
```

---

### 11:51 - 2024-06-24

<details>
<summary>Click for stats</summary>

```json
{
"number_of_projects": 193 
,
"number_of_projects_by_cities": {
    "Paris": 37,
    "Lyon": 22,
    "Cotonou": 19,
    "Toulouse": 14,
    "Montpellier": 13,
    "Strasbourg": 12,
    "Nice": 10,
    "Marseille": 10,
    "Rennes": 10,
    "Bordeaux": 9,
    "Lille": 8,
    "Nancy": 8,
    "Nantes": 7,
    "La R\u00e9union": 6,
    "Barcelona": 4,
    "Mulhouse": 2,
    "Berlin": 1,
    "Bruxelles": 1
} 
,
"status_all_cities": {
    "waiting_update": 73,
    "rejected": 64,
    "approved": 29,
    "draft": 27
} 
,
"status_by_cities": {
    "Cotonou": {
        "draft": 17,
        "waiting_update": 1,
        "rejected": 1
    },
    "La R\u00e9union": {
        "waiting_update": 6
    },
    "Lille": {
        "rejected": 3,
        "waiting_update": 3,
        "approved": 2
    },
    "Nantes": {
        "approved": 3,
        "rejected": 2,
        "draft": 1,
        "waiting_update": 1
    },
    "Lyon": {
        "waiting_update": 11,
        "rejected": 7,
        "approved": 3,
        "draft": 1
    },
    "Paris": {
        "rejected": 15,
        "waiting_update": 11,
        "approved": 7,
        "draft": 4
    },
    "Toulouse": {
        "waiting_update": 7,
        "rejected": 6,
        "draft": 1
    },
    "Nice": {
        "waiting_update": 4,
        "rejected": 3,
        "approved": 2,
        "draft": 1
    },
    "Nancy": {
        "rejected": 4,
        "waiting_update": 3,
        "approved": 1
    },
    "Strasbourg": {
        "rejected": 7,
        "waiting_update": 2,
        "approved": 2,
        "draft": 1
    },
    "Marseille": {
        "rejected": 5,
        "waiting_update": 4,
        "approved": 1
    },
    "Montpellier": {
        "rejected": 6,
        "waiting_update": 5,
        "approved": 1,
        "draft": 1
    },
    "Bordeaux": {
        "rejected": 4,
        "waiting_update": 4,
        "approved": 1
    },
    "Rennes": {
        "waiting_update": 6,
        "approved": 3,
        "rejected": 1
    },
    "Barcelona": {
        "approved": 3,
        "waiting_update": 1
    },
    "Mulhouse": {
        "waiting_update": 2
    },
    "Berlin": {
        "waiting_update": 1
    },
    "Bruxelles": {
        "waiting_update": 1
    }
}
}
```

</details>

### 13:45 - 2024-06-24

<details>
<summary>Click for stats</summary>

```json
{
"number_of_projects": 194 
,
"number_of_projects_by_cities": {
    "Paris": 37,
    "Lyon": 22,
    "Cotonou": 19,
    "Toulouse": 14,
    "Strasbourg": 13,
    "Montpellier": 13,
    "Nice": 10,
    "Marseille": 10,
    "Rennes": 10,
    "Bordeaux": 9,
    "Lille": 8,
    "Nancy": 8,
    "Nantes": 7,
    "La R\u00e9union": 6,
    "Barcelona": 4,
    "Mulhouse": 2,
    "Berlin": 1,
    "Bruxelles": 1
} 
,
"status_all_cities": {
    "waiting_update": 73,
    "rejected": 64,
    "approved": 29,
    "draft": 28
} 
,
"status_by_cities": {
    "Strasbourg": {
        "rejected": 7,
        "draft": 2,
        "waiting_update": 2,
        "approved": 2
    },
    "Cotonou": {
        "draft": 17,
        "waiting_update": 1,
        "rejected": 1
    },
    "La R\u00e9union": {
        "waiting_update": 6
    },
    "Lille": {
        "rejected": 3,
        "waiting_update": 3,
        "approved": 2
    },
    "Nantes": {
        "approved": 3,
        "rejected": 2,
        "draft": 1,
        "waiting_update": 1
    },
    "Lyon": {
        "waiting_update": 11,
        "rejected": 7,
        "approved": 3,
        "draft": 1
    },
    "Paris": {
        "rejected": 15,
        "waiting_update": 11,
        "approved": 7,
        "draft": 4
    },
    "Toulouse": {
        "waiting_update": 7,
        "rejected": 6,
        "draft": 1
    },
    "Nice": {
        "waiting_update": 4,
        "rejected": 3,
        "approved": 2,
        "draft": 1
    },
    "Nancy": {
        "rejected": 4,
        "waiting_update": 3,
        "approved": 1
    },
    "Marseille": {
        "rejected": 5,
        "waiting_update": 4,
        "approved": 1
    },
    "Montpellier": {
        "rejected": 6,
        "waiting_update": 5,
        "approved": 1,
        "draft": 1
    },
    "Bordeaux": {
        "rejected": 4,
        "waiting_update": 4,
        "approved": 1
    },
    "Rennes": {
        "waiting_update": 6,
        "approved": 3,
        "rejected": 1
    },
    "Barcelona": {
        "approved": 3,
        "waiting_update": 1
    },
    "Mulhouse": {
        "waiting_update": 2
    },
    "Berlin": {
        "waiting_update": 1
    },
    "Bruxelles": {
        "waiting_update": 1
    }
} 
,
"number_by_envisaged_type": {
    "solution": 129,
    "entrepreneurship": 41,
    "technical": 24
} 
,
"status_by_envisaged_type": {
    "technical": {
        "waiting_update": 8,
        "approved": 8,
        "rejected": 5,
        "draft": 3
    },
    "solution": {
        "waiting_update": 50,
        "rejected": 41,
        "draft": 21,
        "approved": 17
    },
    "entrepreneurship": {
        "rejected": 18,
        "waiting_update": 15,
        "approved": 4,
        "draft": 4
    }
} 
,
}
```

</details>

### 18:59 - 2024-06-24

<details>
<summary>Click for stats</summary>

```json
{
    "number_of_projects": 204,
    "number_of_projects_by_cities": {
        "Paris": 40,
        "Lyon": 25,
        "Cotonou": 19,
        "Toulouse": 16,
        "Strasbourg": 13,
        "Montpellier": 13,
        "Rennes": 11,
        "Nice": 10,
        "Marseille": 10,
        "Lille": 9,
        "Bordeaux": 9,
        "Nancy": 8,
        "Nantes": 7,
        "La R\u00e9union": 6,
        "Barcelona": 4,
        "Mulhouse": 2,
        "Berlin": 1,
        "Bruxelles": 1
    },
    "status_all_cities": {
        "waiting_update": 70,
        "rejected": 63,
        "draft": 37,
        "approved": 29,
        "pending": 5
    },
    "status_by_cities": {
        "Lyon": {
            "waiting_update": 9,
            "rejected": 7,
            "pending": 3,
            "draft": 3,
            "approved": 3
        },
        "Paris": {
            "rejected": 15,
            "waiting_update": 11,
            "draft": 7,
            "approved": 7
        },
        "Toulouse": {
            "waiting_update": 7,
            "rejected": 6,
            "draft": 3
        },
        "Rennes": {
            "waiting_update": 6,
            "approved": 3,
            "draft": 1,
            "rejected": 1
        },
        "Lille": {
            "rejected": 3,
            "approved": 2,
            "waiting_update": 2,
            "draft": 1,
            "pending": 1
        },
        "Strasbourg": {
            "rejected": 7,
            "draft": 2,
            "waiting_update": 2,
            "approved": 2
        },
        "Cotonou": {
            "draft": 17,
            "waiting_update": 1,
            "rejected": 1
        },
        "La R\u00e9union": {
            "waiting_update": 6
        },
        "Nantes": {
            "approved": 3,
            "rejected": 2,
            "draft": 1,
            "waiting_update": 1
        },
        "Nice": {
            "waiting_update": 4,
            "approved": 2,
            "rejected": 2,
            "draft": 1,
            "pending": 1
        },
        "Nancy": {
            "rejected": 4,
            "waiting_update": 3,
            "approved": 1
        },
        "Marseille": {
            "rejected": 5,
            "waiting_update": 4,
            "approved": 1
        },
        "Montpellier": {
            "rejected": 6,
            "waiting_update": 5,
            "approved": 1,
            "draft": 1
        },
        "Bordeaux": {
            "rejected": 4,
            "waiting_update": 4,
            "approved": 1
        },
        "Barcelona": {
            "approved": 3,
            "waiting_update": 1
        },
        "Mulhouse": {
            "waiting_update": 2
        },
        "Berlin": {
            "waiting_update": 1
        },
        "Bruxelles": {
            "waiting_update": 1
        }
    },
    "number_by_envisaged_type": {
        "solution": 136,
        "entrepreneurship": 42,
        "technical": 26
    },
    "status_by_envisaged_type": {
        "entrepreneurship": {
            "rejected": 18,
            "waiting_update": 14,
            "draft": 4,
            "approved": 4,
            "pending": 2
        },
        "solution": {
            "waiting_update": 48,
            "rejected": 40,
            "draft": 28,
            "approved": 17,
            "pending": 3
        },
        "technical": {
            "waiting_update": 8,
            "approved": 8,
            "draft": 5,
            "rejected": 5
        }
    }
}
```

</details>

### 09:53 - 2024-06-25

<details>
<summary>Click for stats</summary>

```json
{
    "number_of_projects": 207,
    "number_of_projects_by_cities": {
        "Paris": 41,
        "Lyon": 26,
        "Cotonou": 19,
        "Toulouse": 16,
        "Strasbourg": 13,
        "Montpellier": 13,
        "Rennes": 11,
        "Lille": 10,
        "Nice": 10,
        "Marseille": 10,
        "Bordeaux": 9,
        "Nancy": 8,
        "Nantes": 7,
        "La R\u00e9union": 6,
        "Barcelona": 4,
        "Mulhouse": 2,
        "Berlin": 1,
        "Bruxelles": 1
    },
    "status_all_cities": {
        "waiting_update": 69,
        "rejected": 63,
        "draft": 40,
        "approved": 29,
        "pending": 6
    },
    "status_by_cities": {
        "Lille": {
            "rejected": 3,
            "draft": 2,
            "approved": 2,
            "waiting_update": 2,
            "pending": 1
        },
        "Paris": {
            "rejected": 15,
            "waiting_update": 11,
            "draft": 8,
            "approved": 7
        },
        "Lyon": {
            "waiting_update": 8,
            "rejected": 7,
            "draft": 4,
            "pending": 4,
            "approved": 3
        },
        "Toulouse": {
            "waiting_update": 7,
            "rejected": 6,
            "draft": 3
        },
        "Rennes": {
            "waiting_update": 6,
            "approved": 3,
            "draft": 1,
            "rejected": 1
        },
        "Strasbourg": {
            "rejected": 7,
            "draft": 2,
            "waiting_update": 2,
            "approved": 2
        },
        "Cotonou": {
            "draft": 17,
            "waiting_update": 1,
            "rejected": 1
        },
        "La R\u00e9union": {
            "waiting_update": 6
        },
        "Nantes": {
            "approved": 3,
            "rejected": 2,
            "draft": 1,
            "waiting_update": 1
        },
        "Nice": {
            "waiting_update": 4,
            "approved": 2,
            "rejected": 2,
            "draft": 1,
            "pending": 1
        },
        "Nancy": {
            "rejected": 4,
            "waiting_update": 3,
            "approved": 1
        },
        "Marseille": {
            "rejected": 5,
            "waiting_update": 4,
            "approved": 1
        },
        "Montpellier": {
            "rejected": 6,
            "waiting_update": 5,
            "approved": 1,
            "draft": 1
        },
        "Bordeaux": {
            "rejected": 4,
            "waiting_update": 4,
            "approved": 1
        },
        "Barcelona": {
            "approved": 3,
            "waiting_update": 1
        },
        "Mulhouse": {
            "waiting_update": 2
        },
        "Berlin": {
            "waiting_update": 1
        },
        "Bruxelles": {
            "waiting_update": 1
        }
    },
    "number_by_envisaged_type": {
        "solution": 137,
        "entrepreneurship": 43,
        "technical": 27
    },
    "status_by_envisaged_type": {
        "solution": {
            "waiting_update": 48,
            "rejected": 40,
            "draft": 29,
            "approved": 17,
            "pending": 3
        },
        "technical": {
            "approved": 8,
            "waiting_update": 7,
            "draft": 6,
            "rejected": 5,
            "pending": 1
        },
        "entrepreneurship": {
            "rejected": 18,
            "waiting_update": 14,
            "draft": 5,
            "approved": 4,
            "pending": 2
        }
    },
    "number_status_by_tags": {
        "Video Games": {
            "waiting_update": 11,
            "rejected": 8,
            "draft": 7,
            "approved": 5
        },
        "Green Technologies": {
            "waiting_update": 2,
            "draft": 1
        },
        "Bioinformatics": {
            "draft": 1
        },
        "Web Development": {
            "rejected": 23,
            "waiting_update": 21,
            "draft": 12,
            "approved": 7,
            "pending": 1
        },
        "Blockchain": {
            "draft": 4,
            "rejected": 2,
            "approved": 2,
            "waiting_update": 2
        },
        "Open Source": {
            "rejected": 4,
            "approved": 4,
            "waiting_update": 3,
            "draft": 2
        },
        "Automation": {
            "waiting_update": 12,
            "rejected": 4,
            "draft": 3,
            "approved": 2,
            "pending": 1
        },
        "Esport": {
            "rejected": 2,
            "draft": 1,
            "waiting_update": 1
        },
        "Educational Technologies": {
            "waiting_update": 10,
            "rejected": 8,
            "approved": 3,
            "draft": 2,
            "pending": 1
        },
        "Collaborative Design": {
            "waiting_update": 2,
            "pending": 1,
            "rejected": 1
        },
        "Mobile Applications": {
            "waiting_update": 31,
            "rejected": 28,
            "draft": 14,
            "approved": 7,
            "pending": 2
        },
        "Streaming": {
            "approved": 2,
            "draft": 1
        },
        "HealthTech": {
            "rejected": 4,
            "waiting_update": 3,
            "approved": 3,
            "draft": 2
        },
        "Entertainment Computing": {
            "waiting_update": 6,
            "draft": 2,
            "approved": 2,
            "rejected": 1
        },
        "Cybersecurity": {
            "draft": 3,
            "approved": 3,
            "waiting_update": 2,
            "rejected": 1
        },
        "Data Management": {
            "draft": 6,
            "rejected": 5,
            "waiting_update": 1,
            "approved": 1
        },
        "Machine Learning": {
            "waiting_update": 14,
            "rejected": 9,
            "approved": 7,
            "draft": 5,
            "pending": 1
        },
        "Social Innovation": {
            "rejected": 6,
            "draft": 3,
            "approved": 3,
            "waiting_update": 2
        },
        "Tech for Good": {
            "waiting_update": 7,
            "approved": 6,
            "rejected": 3,
            "draft": 2,
            "pending": 1
        },
        "Big Data": {
            "waiting_update": 2,
            "draft": 1,
            "rejected": 1
        },
        "Data Analysis": {
            "waiting_update": 9,
            "rejected": 9,
            "draft": 5,
            "approved": 4,
            "pending": 1
        },
        "3D Modeling": {
            "draft": 4,
            "waiting_update": 2,
            "rejected": 2
        },
        "Assistive Technologies": {
            "rejected": 4,
            "draft": 2,
            "waiting_update": 2,
            "approved": 1
        },
        "Social Networks": {
            "rejected": 8,
            "waiting_update": 5,
            "draft": 1
        },
        "Voice Recognition": {
            "waiting_update": 3,
            "approved": 1
        },
        "Digital Transformation": {
            "approved": 2,
            "waiting_update": 2,
            "rejected": 1
        },
        "Geolocation": {
            "rejected": 4,
            "draft": 2,
            "waiting_update": 1,
            "approved": 1
        },
        "Product Design": {
            "waiting_update": 1,
            "rejected": 1
        },
        "Hybrid Applications": {
            "draft": 2,
            "waiting_update": 1,
            "rejected": 1
        },
        "E-commerce": {
            "waiting_update": 2,
            "rejected": 2,
            "draft": 1
        },
        "Robotics": {
            "waiting_update": 4,
            "rejected": 1
        },
        "Sharing Platforms": {
            "rejected": 4,
            "draft": 2,
            "waiting_update": 1
        },
        "Web Services": {
            "rejected": 8,
            "waiting_update": 4,
            "pending": 2,
            "draft": 1
        },
        "Management Computing": {
            "rejected": 3,
            "waiting_update": 2,
            "pending": 1,
            "approved": 1
        },
        "Knowledge Management": {
            "draft": 1,
            "waiting_update": 1
        },
        "Connected Computing": {
            "draft": 1
        },
        "Agricultural Computing": {
            "draft": 1,
            "waiting_update": 1,
            "rejected": 1,
            "pending": 1
        },
        "Project Management": {
            "rejected": 3,
            "waiting_update": 2
        },
        "AR/VR": {
            "approved": 4,
            "draft": 2,
            "waiting_update": 1,
            "rejected": 1
        },
        "Mobile Computing": {
            "rejected": 2
        },
        "Immersive Technologies": {
            "waiting_update": 2,
            "draft": 1
        },
        "Human-Machine Interaction": {
            "waiting_update": 2,
            "rejected": 2
        },
        "Smart Cities": {
            "rejected": 1
        },
        "High Performance Computing": {
            "pending": 1,
            "approved": 1
        },
        "Game Design": {
            "waiting_update": 4,
            "approved": 3,
            "rejected": 2,
            "draft": 1
        },
        "Internet of Things": {
            "waiting_update": 2
        },
        "Predictive Analytics": {
            "pending": 1,
            "rejected": 1
        },
        "DevOps": {
            "waiting_update": 3,
            "approved": 3
        },
        "FinTech": {
            "approved": 2,
            "waiting_update": 1
        },
        "Cryptocurrencies": {
            "waiting_update": 2
        },
        "Distributed Computing": {
            "approved": 1
        },
        "Signal Processing": {
            "approved": 1,
            "waiting_update": 1
        },
        "Mathematical Modeling": {
            "approved": 1,
            "waiting_update": 1
        },
        "Agile Development": {
            "waiting_update": 1,
            "rejected": 1
        },
        "Renewable Energy": {
            "waiting_update": 1
        },
        "M2M Communication": {
            "rejected": 1
        },
        "Animaux": {
            "waiting_update": 1
        }
    }
}
```

</details>

### 20:02 - 2024-06-25

<details>
<summary>Click for stats</summary>

```json
{
    "number_of_projects": 223,
    "number_of_projects_by_cities": {
        "Paris": 46,
        "Lyon": 27,
        "Cotonou": 19,
        "Toulouse": 16,
        "Strasbourg": 15,
        "Montpellier": 13,
        "Marseille": 12,
        "Lille": 12,
        "Nice": 11,
        "Rennes": 11,
        "Bordeaux": 10,
        "Nancy": 9,
        "Nantes": 8,
        "La R\u00e9union": 6,
        "Barcelona": 4,
        "Mulhouse": 2,
        "Berlin": 1,
        "Bruxelles": 1
    },
    "status_all_cities": {
        "waiting_update": 65,
        "rejected": 63,
        "draft": 57,
        "approved": 29,
        "pending": 9
    },
    "status_by_cities": {
        "Paris": {
            "rejected": 15,
            "draft": 13,
            "waiting_update": 11,
            "approved": 7
        },
        "Strasbourg": {
            "rejected": 7,
            "draft": 4,
            "waiting_update": 2,
            "approved": 2
        },
        "Nantes": {
            "approved": 3,
            "draft": 2,
            "rejected": 2,
            "waiting_update": 1
        },
        "Nancy": {
            "rejected": 4,
            "waiting_update": 3,
            "draft": 1,
            "approved": 1
        },
        "Marseille": {
            "rejected": 5,
            "waiting_update": 3,
            "draft": 2,
            "pending": 1,
            "approved": 1
        },
        "Lyon": {
            "waiting_update": 8,
            "rejected": 7,
            "draft": 5,
            "pending": 4,
            "approved": 3
        },
        "Nice": {
            "waiting_update": 4,
            "draft": 2,
            "approved": 2,
            "rejected": 2,
            "pending": 1
        },
        "Lille": {
            "draft": 4,
            "rejected": 3,
            "approved": 2,
            "pending": 2,
            "waiting_update": 1
        },
        "Bordeaux": {
            "rejected": 4,
            "waiting_update": 4,
            "draft": 1,
            "approved": 1
        },
        "Toulouse": {
            "waiting_update": 7,
            "rejected": 6,
            "draft": 3
        },
        "Rennes": {
            "waiting_update": 6,
            "approved": 3,
            "draft": 1,
            "rejected": 1
        },
        "Cotonou": {
            "draft": 17,
            "waiting_update": 1,
            "rejected": 1
        },
        "La R\u00e9union": {
            "waiting_update": 5,
            "draft": 1
        },
        "Montpellier": {
            "rejected": 6,
            "waiting_update": 4,
            "approved": 1,
            "draft": 1,
            "pending": 1
        },
        "Barcelona": {
            "approved": 3,
            "waiting_update": 1
        },
        "Mulhouse": {
            "waiting_update": 2
        },
        "Berlin": {
            "waiting_update": 1
        },
        "Bruxelles": {
            "waiting_update": 1
        }
    },
    "number_by_envisaged_type": {
        "solution": 145,
        "entrepreneurship": 48,
        "technical": 30
    },
    "status_by_envisaged_type": {
        "solution": {
            "waiting_update": 45,
            "rejected": 40,
            "draft": 38,
            "approved": 17,
            "pending": 5
        },
        "technical": {
            "draft": 8,
            "approved": 8,
            "waiting_update": 7,
            "rejected": 5,
            "pending": 2
        },
        "entrepreneurship": {
            "rejected": 18,
            "waiting_update": 13,
            "draft": 11,
            "approved": 4,
            "pending": 2
        }
    },
    "number_status_by_tags": {
        "Mobile Applications": {
            "waiting_update": 29,
            "rejected": 28,
            "draft": 20,
            "approved": 7,
            "pending": 4
        },
        "HealthTech": {
            "rejected": 4,
            "waiting_update": 3,
            "approved": 3,
            "draft": 2
        },
        "Assistive Technologies": {
            "draft": 4,
            "rejected": 4,
            "waiting_update": 2,
            "approved": 1
        },
        "Web Development": {
            "rejected": 23,
            "waiting_update": 21,
            "draft": 15,
            "approved": 7,
            "pending": 1
        },
        "Automation": {
            "waiting_update": 11,
            "draft": 4,
            "rejected": 4,
            "pending": 2,
            "approved": 2
        },
        "Collaborative Design": {
            "draft": 2,
            "waiting_update": 2,
            "pending": 1,
            "rejected": 1
        },
        "Big Data": {
            "draft": 2,
            "waiting_update": 2,
            "rejected": 1
        },
        "Project Management": {
            "rejected": 3,
            "waiting_update": 2,
            "draft": 1
        },
        "Web Services": {
            "rejected": 8,
            "draft": 4,
            "waiting_update": 4,
            "pending": 2
        },
        "Green Technologies": {
            "draft": 2,
            "waiting_update": 2
        },
        "Tech for Good": {
            "approved": 6,
            "waiting_update": 6,
            "draft": 5,
            "rejected": 3,
            "pending": 2
        },
        "Geolocation": {
            "rejected": 4,
            "draft": 3,
            "waiting_update": 1,
            "approved": 1
        },
        "DevOps": {
            "waiting_update": 3,
            "approved": 3,
            "draft": 1
        },
        "Open Source": {
            "draft": 4,
            "rejected": 4,
            "approved": 4,
            "waiting_update": 3,
            "pending": 1
        },
        "Signal Processing": {
            "draft": 1,
            "approved": 1,
            "waiting_update": 1
        },
        "Mathematical Modeling": {
            "draft": 1,
            "approved": 1,
            "waiting_update": 1
        },
        "Data Analysis": {
            "waiting_update": 9,
            "rejected": 9,
            "draft": 6,
            "approved": 4,
            "pending": 1
        },
        "Video Games": {
            "draft": 12,
            "waiting_update": 10,
            "rejected": 8,
            "approved": 5
        },
        "Game Design": {
            "draft": 3,
            "approved": 3,
            "waiting_update": 3,
            "rejected": 2
        },
        "Cloud Computing": {
            "draft": 1
        },
        "Data Management": {
            "draft": 7,
            "rejected": 5,
            "waiting_update": 1,
            "approved": 1
        },
        "M2M Communication": {
            "draft": 1,
            "rejected": 1
        },
        "Blockchain": {
            "draft": 5,
            "rejected": 2,
            "approved": 2,
            "waiting_update": 2
        },
        "Educational Technologies": {
            "waiting_update": 10,
            "rejected": 8,
            "draft": 3,
            "approved": 3,
            "pending": 1
        },
        "Social Innovation": {
            "rejected": 6,
            "draft": 4,
            "approved": 3,
            "waiting_update": 2
        },
        "Management Computing": {
            "rejected": 3,
            "draft": 2,
            "waiting_update": 2,
            "pending": 1,
            "approved": 1
        },
        "FinTech": {
            "approved": 2,
            "draft": 1,
            "waiting_update": 1
        },
        "E-commerce": {
            "draft": 2,
            "waiting_update": 2,
            "rejected": 2
        },
        "Bioinformatics": {
            "draft": 1
        },
        "Esport": {
            "rejected": 2,
            "draft": 1,
            "waiting_update": 1
        },
        "Streaming": {
            "approved": 2,
            "draft": 1
        },
        "Entertainment Computing": {
            "waiting_update": 6,
            "draft": 2,
            "approved": 2,
            "rejected": 1
        },
        "Cybersecurity": {
            "draft": 3,
            "approved": 3,
            "waiting_update": 2,
            "rejected": 1
        },
        "Machine Learning": {
            "waiting_update": 13,
            "rejected": 9,
            "approved": 7,
            "draft": 5,
            "pending": 3
        },
        "3D Modeling": {
            "draft": 4,
            "rejected": 2,
            "waiting_update": 1
        },
        "Social Networks": {
            "rejected": 8,
            "waiting_update": 5,
            "draft": 1
        },
        "Voice Recognition": {
            "waiting_update": 3,
            "approved": 1
        },
        "Digital Transformation": {
            "approved": 2,
            "waiting_update": 2,
            "rejected": 1
        },
        "Product Design": {
            "waiting_update": 1,
            "rejected": 1
        },
        "Hybrid Applications": {
            "draft": 2,
            "waiting_update": 1,
            "rejected": 1
        },
        "Robotics": {
            "waiting_update": 4,
            "rejected": 1
        },
        "Sharing Platforms": {
            "rejected": 4,
            "draft": 2,
            "waiting_update": 1
        },
        "Knowledge Management": {
            "draft": 1,
            "waiting_update": 1
        },
        "Connected Computing": {
            "draft": 1
        },
        "Agricultural Computing": {
            "draft": 1,
            "waiting_update": 1,
            "rejected": 1,
            "pending": 1
        },
        "AR/VR": {
            "approved": 4,
            "draft": 1,
            "waiting_update": 1,
            "rejected": 1
        },
        "Mobile Computing": {
            "rejected": 2
        },
        "Immersive Technologies": {
            "waiting_update": 2
        },
        "Human-Machine Interaction": {
            "waiting_update": 2,
            "rejected": 2
        },
        "Smart Cities": {
            "rejected": 1
        },
        "High Performance Computing": {
            "pending": 1,
            "approved": 1
        },
        "Internet of Things": {
            "waiting_update": 2
        },
        "Predictive Analytics": {
            "pending": 1,
            "rejected": 1
        },
        "Cryptocurrencies": {
            "waiting_update": 2
        },
        "Distributed Computing": {
            "approved": 1
        },
        "Agile Development": {
            "pending": 1,
            "rejected": 1
        },
        "Renewable Energy": {
            "waiting_update": 1
        },
        "Animaux": {
            "pending": 1
        }
    }
}
```

</details>

### 09:21 - 2024-06-28

<details>
<summary>Click for stats</summary>

```json
{
    "number_of_projects": 258,
    "number_of_projects_by_cities": {
        "Paris": 59,
        "Lyon": 29,
        "Toulouse": 20,
        "Cotonou": 19,
        "Montpellier": 17,
        "Strasbourg": 16,
        "Marseille": 15,
        "Lille": 13,
        "Nancy": 12,
        "Nice": 12,
        "Bordeaux": 12,
        "Rennes": 11,
        "Nantes": 9,
        "La R\u00e9union": 6,
        "Barcelona": 4,
        "Mulhouse": 2,
        "Berlin": 1,
        "Bruxelles": 1
    },
    "status_all_cities": {
        "pending": 144,
        "rejected": 63,
        "approved": 31,
        "draft": 19,
        "waiting_update": 1
    },
    "status_by_cities": {
        "Paris": {
            "pending": 36,
            "rejected": 15,
            "approved": 7,
            "draft": 1
        },
        "Nancy": {
            "pending": 7,
            "rejected": 4,
            "approved": 1
        },
        "Lille": {
            "pending": 8,
            "rejected": 3,
            "approved": 2
        },
        "Lyon": {
            "pending": 19,
            "rejected": 7,
            "approved": 3
        },
        "Montpellier": {
            "pending": 9,
            "rejected": 6,
            "approved": 1,
            "draft": 1
        },
        "Marseille": {
            "pending": 9,
            "rejected": 5,
            "approved": 1
        },
        "Toulouse": {
            "pending": 12,
            "rejected": 6,
            "approved": 2
        },
        "Nantes": {
            "pending": 4,
            "approved": 3,
            "rejected": 2
        },
        "Nice": {
            "pending": 8,
            "approved": 2,
            "rejected": 2
        },
        "Bordeaux": {
            "pending": 7,
            "rejected": 4,
            "approved": 1
        },
        "Strasbourg": {
            "pending": 7,
            "rejected": 7,
            "approved": 2
        },
        "Rennes": {
            "pending": 7,
            "approved": 3,
            "rejected": 1
        },
        "Cotonou": {
            "draft": 17,
            "waiting_update": 1,
            "rejected": 1
        },
        "La R\u00e9union": {
            "pending": 6
        },
        "Barcelona": {
            "approved": 3,
            "pending": 1
        },
        "Mulhouse": {
            "pending": 2
        },
        "Berlin": {
            "pending": 1
        },
        "Bruxelles": {
            "pending": 1
        }
    },
    "number_by_envisaged_type": {
        "solution": 154,
        "entrepreneurship": 63,
        "technical": 41
    },
    "status_by_envisaged_type": {
        "entrepreneurship": {
            "pending": 39,
            "rejected": 19,
            "approved": 4,
            "draft": 1
        },
        "solution": {
            "pending": 79,
            "rejected": 39,
            "approved": 18,
            "draft": 17,
            "waiting_update": 1
        },
        "technical": {
            "pending": 26,
            "approved": 9,
            "rejected": 5,
            "draft": 1
        }
    },
    "number_status_by_tags": {
        "Mobile Applications": {
            "pending": 57,
            "rejected": 28,
            "draft": 9,
            "approved": 8,
            "waiting_update": 1
        },
        "Data Management": {
            "pending": 8,
            "rejected": 5,
            "draft": 3,
            "approved": 1
        },
        "Digital Transformation": {
            "pending": 3,
            "approved": 2,
            "rejected": 1
        },
        "Web Development": {
            "pending": 35,
            "rejected": 23,
            "approved": 8,
            "draft": 7,
            "waiting_update": 1
        },
        "Automation": {
            "pending": 19,
            "rejected": 3,
            "approved": 3,
            "draft": 1
        },
        "Video Games": {
            "pending": 31,
            "rejected": 8,
            "approved": 5,
            "draft": 1
        },
        "Educational Technologies": {
            "pending": 20,
            "rejected": 8,
            "approved": 3,
            "draft": 2
        },
        "Game Design": {
            "pending": 8,
            "approved": 3,
            "rejected": 2
        },
        "AR/VR": {
            "pending": 4,
            "approved": 4,
            "draft": 1,
            "rejected": 1
        },
        "Tech for Good": {
            "pending": 20,
            "approved": 6,
            "rejected": 3
        },
        "Machine Learning": {
            "pending": 26,
            "approved": 9,
            "rejected": 9,
            "draft": 3
        },
        "Management Computing": {
            "pending": 5,
            "rejected": 3,
            "approved": 1
        },
        "Human-Machine Interaction": {
            "pending": 5,
            "rejected": 2
        },
        "Predictive Analytics": {
            "pending": 3,
            "rejected": 1
        },
        "Social Networks": {
            "rejected": 8,
            "pending": 6,
            "approved": 1,
            "draft": 1
        },
        "Hybrid Applications": {
            "pending": 5,
            "draft": 1,
            "rejected": 1
        },
        "Esport": {
            "pending": 3,
            "rejected": 2
        },
        "Signal Processing": {
            "pending": 3,
            "approved": 1
        },
        "Open Source": {
            "pending": 12,
            "rejected": 4,
            "approved": 4
        },
        "Sharing Platforms": {
            "rejected": 4,
            "pending": 3,
            "draft": 2
        },
        "3D Modeling": {
            "pending": 10,
            "rejected": 2
        },
        "HealthTech": {
            "pending": 6,
            "rejected": 4,
            "approved": 3,
            "waiting_update": 1
        },
        "High Performance Computing": {
            "pending": 2,
            "approved": 1
        },
        "Big Data": {
            "pending": 4,
            "rejected": 1
        },
        "Data Analysis": {
            "pending": 16,
            "rejected": 9,
            "approved": 4,
            "draft": 3
        },
        "Web Services": {
            "pending": 12,
            "rejected": 8,
            "draft": 1
        },
        "Assistive Technologies": {
            "pending": 7,
            "rejected": 4,
            "draft": 1,
            "approved": 1
        },
        "Social Innovation": {
            "pending": 7,
            "rejected": 6,
            "approved": 3,
            "draft": 2
        },
        "Entertainment Computing": {
            "pending": 10,
            "approved": 2,
            "rejected": 1
        },
        "Cybersecurity": {
            "pending": 4,
            "approved": 3,
            "rejected": 1,
            "draft": 1
        },
        "Blockchain": {
            "pending": 7,
            "rejected": 3,
            "approved": 2
        },
        "Geolocation": {
            "rejected": 4,
            "pending": 3,
            "draft": 2,
            "approved": 1
        },
        "Immersive Technologies": {
            "pending": 3
        },
        "Collaborative Design": {
            "pending": 5,
            "rejected": 1
        },
        "Project Management": {
            "pending": 3,
            "rejected": 3
        },
        "Green Technologies": {
            "pending": 4
        },
        "Mathematical Modeling": {
            "pending": 2,
            "approved": 1
        },
        "Cloud Computing": {
            "pending": 1
        },
        "M2M Communication": {
            "pending": 1,
            "rejected": 1
        },
        "E-commerce": {
            "pending": 3,
            "rejected": 2,
            "draft": 1
        },
        "Streaming": {
            "approved": 2,
            "pending": 1
        },
        "Voice Recognition": {
            "pending": 4,
            "approved": 1
        },
        "Product Design": {
            "pending": 1,
            "rejected": 1
        },
        "Robotics": {
            "pending": 3,
            "rejected": 1
        },
        "Knowledge Management": {
            "draft": 1,
            "pending": 1
        },
        "Connected Computing": {
            "draft": 1
        },
        "Agricultural Computing": {
            "draft": 1,
            "rejected": 1,
            "pending": 1
        },
        "Mobile Computing": {
            "rejected": 2
        },
        "Smart Cities": {
            "rejected": 1
        },
        "Internet of Things": {
            "pending": 2
        },
        "DevOps": {
            "pending": 3,
            "approved": 3
        },
        "FinTech": {
            "approved": 2,
            "pending": 1
        },
        "Cryptocurrencies": {
            "pending": 2
        },
        "Distributed Computing": {
            "approved": 1
        },
        "Agile Development": {
            "pending": 1,
            "rejected": 1
        },
        "Renewable Energy": {
            "pending": 1
        },
        "Animaux": {
            "pending": 1
        }
    }
}
```

</details>

### 23:23 - 2025-01-27

<details>
<summary>Click for stats (year 2023)</summary>

```bash
eiptek3api --year 2023 --include-rejected
```

```json
{
    "number_of_projects": 258,
    "number_of_projects_by_cities": {
        "Paris": 59,
        "Lyon": 29,
        "Toulouse": 19,
        "Cotonou": 19,
        "Montpellier": 17,
        "Strasbourg": 16,
        "Lille": 15,
        "Marseille": 15,
        "Bordeaux": 13,
        "Nancy": 12,
        "Nice": 12,
        "Nantes": 9,
        "Rennes": 9,
        "La R\u00e9union": 6,
        "Barcelona": 4,
        "Mulhouse": 2,
        "Berlin": 1,
        "Bruxelles": 1
    },
    "status_all_cities": {
        "approved": 162,
        "rejected": 78,
        "draft": 18
    },
    "status_by_cities": {
        "Paris": {
            "approved": 38,
            "rejected": 21
        },
        "Nancy": {
            "approved": 8,
            "rejected": 4
        },
        "Lille": {
            "approved": 11,
            "rejected": 4
        },
        "Lyon": {
            "approved": 18,
            "rejected": 11
        },
        "Montpellier": {
            "approved": 9,
            "rejected": 7,
            "draft": 1
        },
        "Marseille": {
            "approved": 9,
            "rejected": 6
        },
        "Toulouse": {
            "approved": 13,
            "rejected": 6
        },
        "Nantes": {
            "approved": 6,
            "rejected": 3
        },
        "Nice": {
            "approved": 9,
            "rejected": 3
        },
        "Bordeaux": {
            "approved": 9,
            "rejected": 4
        },
        "Strasbourg": {
            "approved": 9,
            "rejected": 7
        },
        "Rennes": {
            "approved": 8,
            "rejected": 1
        },
        "Cotonou": {
            "draft": 17,
            "approved": 1,
            "rejected": 1
        },
        "La R\u00e9union": {
            "approved": 6
        },
        "Barcelona": {
            "approved": 4
        },
        "Mulhouse": {
            "approved": 2
        },
        "Berlin": {
            "approved": 1
        },
        "Bruxelles": {
            "approved": 1
        }
    },
    "number_by_envisaged_type": {
        "solution": 156,
        "entrepreneurship": 63,
        "technical": 39
    },
    "status_by_envisaged_type": {
        "entrepreneurship": {
            "approved": 35,
            "rejected": 27,
            "draft": 1
        },
        "solution": {
            "approved": 94,
            "rejected": 46,
            "draft": 16
        },
        "technical": {
            "approved": 33,
            "rejected": 5,
            "draft": 1
        }
    },
    "number_status_by_tags": {
        "Mobile Applications": {
            "approved": 57,
            "rejected": 38,
            "draft": 9
        },
        "Data Management": {
            "approved": 9,
            "rejected": 5,
            "draft": 3
        },
        "Digital Transformation": {
            "approved": 5,
            "rejected": 1
        },
        "Web Development": {
            "approved": 41,
            "rejected": 26,
            "draft": 7
        },
        "Automation": {
            "approved": 20,
            "rejected": 4,
            "draft": 1
        },
        "Video Games": {
            "approved": 36,
            "rejected": 8,
            "draft": 1
        },
        "Educational Technologies": {
            "approved": 20,
            "rejected": 11,
            "draft": 2
        },
        "Game Design": {
            "approved": 11,
            "rejected": 2
        },
        "AR/VR": {
            "approved": 8,
            "draft": 1,
            "rejected": 1
        },
        "Tech for Good": {
            "approved": 23,
            "rejected": 6
        },
        "Machine Learning": {
            "approved": 34,
            "rejected": 11,
            "draft": 3
        },
        "Management Computing": {
            "approved": 5,
            "rejected": 4
        },
        "Human-Machine Interaction": {
            "rejected": 4,
            "approved": 3
        },
        "Predictive Analytics": {
            "approved": 3,
            "rejected": 1
        },
        "Social Networks": {
            "rejected": 8,
            "approved": 7,
            "draft": 1
        },
        "Hybrid Applications": {
            "approved": 4,
            "rejected": 3
        },
        "Esport": {
            "approved": 3,
            "rejected": 2
        },
        "Signal Processing": {
            "approved": 4
        },
        "Open Source": {
            "approved": 14,
            "rejected": 5
        },
        "Sharing Platforms": {
            "rejected": 5,
            "approved": 3,
            "draft": 1
        },
        "3D Modeling": {
            "approved": 10,
            "rejected": 2
        },
        "HealthTech": {
            "approved": 7,
            "rejected": 6
        },
        "High Performance Computing": {
            "approved": 3
        },
        "Big Data": {
            "approved": 4,
            "rejected": 1
        },
        "Data Analysis": {
            "approved": 18,
            "rejected": 11,
            "draft": 3
        },
        "Web Services": {
            "approved": 10,
            "rejected": 10,
            "draft": 1
        },
        "Assistive Technologies": {
            "approved": 6,
            "rejected": 6,
            "draft": 1
        },
        "Social Innovation": {
            "approved": 9,
            "rejected": 7,
            "draft": 2
        },
        "Entertainment Computing": {
            "approved": 12,
            "rejected": 1
        },
        "Cybersecurity": {
            "approved": 7,
            "rejected": 1,
            "draft": 1
        },
        "Blockchain": {
            "approved": 7,
            "rejected": 4
        },
        "Geolocation": {
            "rejected": 5,
            "approved": 3,
            "draft": 2
        },
        "Immersive Technologies": {
            "approved": 3
        },
        "Collaborative Design": {
            "approved": 4,
            "rejected": 2
        },
        "Project Management": {
            "approved": 3,
            "rejected": 3
        },
        "Green Technologies": {
            "approved": 3,
            "rejected": 1
        },
        "Mathematical Modeling": {
            "approved": 3
        },
        "Cloud Computing": {
            "approved": 1
        },
        "M2M Communication": {
            "approved": 1,
            "rejected": 1
        },
        "E-commerce": {
            "approved": 3,
            "rejected": 2,
            "draft": 1
        },
        "Streaming": {
            "approved": 3
        },
        "Voice Recognition": {
            "approved": 5
        },
        "Product Design": {
            "approved": 1,
            "rejected": 1
        },
        "Robotics": {
            "approved": 3,
            "rejected": 1
        },
        "Knowledge Management": {
            "draft": 1,
            "approved": 1
        },
        "Connected Computing": {
            "draft": 1
        },
        "Agricultural Computing": {
            "draft": 1,
            "rejected": 1,
            "approved": 1
        },
        "Mobile Computing": {
            "rejected": 2
        },
        "Smart Cities": {
            "rejected": 1
        },
        "Internet of Things": {
            "approved": 2
        },
        "DevOps": {
            "approved": 6
        },
        "FinTech": {
            "approved": 3
        },
        "Cryptocurrencies": {
            "approved": 2
        },
        "Distributed Computing": {
            "approved": 1
        },
        "Agile Development": {
            "approved": 1,
            "rejected": 1
        },
        "Renewable Energy": {
            "approved": 1
        },
        "Animaux": {
            "approved": 1
        }
    }
}
```
