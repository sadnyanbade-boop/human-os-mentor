# data.py

# --- 1. SYLLABUS DATABASE ---
MAHARASHTRA_SYLLABUS = {
    "Class 10 (SSC)": {
        "Science 1": ["Gravitation", "Periodic Classification", "Chemical Reactions", "Electric Current", "Heat", "Refraction of Light", "Lenses", "Metallurgy", "Carbon Compounds", "Space Missions"],
        "Science 2": ["Heredity", "Life Processes 1", "Life Processes 2", "Environment", "Green Energy", "Animal Classification", "Microbiology", "Cell Biology", "Social Health", "Disaster Management"],
        "Maths 1": ["Linear Equations", "Quadratic Equations", "Arithmetic Progression", "Financial Planning", "Probability", "Statistics"]
    },
    "Class 9 (SSC)": {
        "Science": ["Laws of Motion", "Work and Energy", "Current Electricity", "Measurement of Matter", "Acids, Bases and Salts", "Classification of Plants", "Energy Flow in Ecosystem", "Useful and Harmful Microbes", "Environmental Management", "Information Communication Technology"],
        "Maths 1": ["Sets", "Real Numbers", "Polynomials", "Ratio and Proportion", "Linear Equations in Two Variables", "Financial Planning", "Statistics"],
        "Maths 2": ["Basic Concepts in Geometry", "Parallel Lines", "Triangles", "Construction of Triangles", "Quadrilaterals", "Circle", "Coordinate Geometry", "Trigonometry", "Surface Area and Volume"]
    }
}

# --- 2. IMPORTANT CONCEPTS ---
IMPORTANT_CONCEPTS = {
    "English": {
        # CLASS 10
        "Gravitation": ["Newton's Universal Law", "Kepler's Laws", "Escape Velocity", "Free Fall"],
        "Periodic Classification": ["Modern Periodic Table", "Valency", "Metallic Character", "Dobereiner's Triads"],
        "Chemical Reactions": ["Types of Reactions", "Oxidation & Reduction", "Corrosion", "Balancing Equations"],
        "Electric Current": ["Ohm's Law", "Electric Motor", "Fleming's Left Hand Rule", "AC vs DC Current"],
        "Heat": ["Latent Heat", "Anomalous Behavior of Water", "Specific Heat Capacity", "Dew Point"],
        "Refraction of Light": ["Laws of Refraction", "Dispersion of Light", "Mirage Effect", "Refractive Index"],
        "Lenses": ["Human Eye Anatomy", "Myopia vs Hypermetropia", "Power of Lens", "Sign Convention"],
        "Metallurgy": ["Blast Furnace", "Extraction of Aluminium", "Corrosion Prevention", "Anodization"],
        "Carbon Compounds": ["Catenation Power", "Functional Groups", "IUPAC Naming", "Soaps and Detergents"],
        "Space Missions": ["Artificial Satellites", "Types of Orbits", "Space Debris", "Escape Velocity"],
        "Heredity": ["DNA & RNA", "Darwin's Theory", "Transcription", "Human Evolution"],
        "Life Processes 1": ["Glycolysis", "Mitosis vs Meiosis", "Aerobic Respiration", "ATP Energy"],
        "Life Processes 2": ["Flower Reproduction", "Menstrual Cycle", "IVF", "Reproductive Systems"],
        "Green Energy": ["Hydroelectric Power", "Wind Energy", "Solar Energy", "Nuclear Energy"],
        "Animal Classification": ["Chordates", "Mammals", "Pisces", "Reptilia"],
        "Microbiology": ["Probiotics", "Industrial Microbiology", "Antibiotics", "Biofuels"],
        "Cell Biology": ["Stem Cells", "Biotechnology", "GMO", "Cloning"],
        "Linear Equations": ["Cramer's Rule", "Graphical Method", "Substitution Method"],
        "Quadratic Equations": ["Formula Method", "Factorization", "Nature of Roots"],
        "Arithmetic Progression": ["nth Term (tn)", "Sum of n Terms (Sn)", "Sequence Logic"],
        "Financial Planning": ["GST Calculation", "Shares & Dividends", "SIP & Mutual Funds"],
        "Probability": ["Sample Space", "Events", "Coin Toss", "Dice Roll"],
        "Statistics": ["Mean", "Histogram", "Pie Diagram", "Median"],
        
        # CLASS 9
        "Laws of Motion": ["Newton's Laws", "Speed vs Velocity", "Acceleration"],
        "Work and Energy": ["Kinetic Energy", "Potential Energy", "Law of Conservation"],
        "Current Electricity": ["Ohm's Law", "Resistors in Series", "Resistors in Parallel"],
        "Measurement of Matter": ["Mole Concept", "Avogadro's Number", "Atom Structure"],
        "Acids, Bases and Salts": ["pH Scale", "Neutralization", "Indicators"],
        "Classification of Plants": ["Thallophyta", "Bryophyta", "Pteridophyta"],
        "Energy Flow in Ecosystem": ["Food Chain", "Food Web", "Energy Pyramid"],
        "Useful and Harmful Microbes": ["Lactobacilli", "Rhizobium", "Antibiotics"],
        "Sets": ["Venn Diagrams", "Union & Intersection", "Subset"],
        "Real Numbers": ["Rational vs Irrational", "Surds", "Rationalization"],
        "Polynomials": ["Degree of Polynomial", "Remainder Theorem", "Factor Theorem"],
        "Ratio and Proportion": ["Direct Variation", "Inverse Variation", "K-method"],
        "Linear Equations in Two Variables": ["Elimination Method", "Substitution Method"],
        "Basic Concepts in Geometry": ["Coordinates", "Betweenness", "Conditional Statements"],
        "Parallel Lines": ["Corresponding Angles", "Alternate Angles", "Interior Angles"],
        "Triangles": ["Congruence Tests", "Isosceles Triangle Theorem", "Median"],
        "Quadrilaterals": ["Parallelogram Properties", "Midpoint Theorem", "Rhombus"],
        "Circle": ["Chords & Arcs", "Tangent Theorems", "Cyclic Quadrilateral"],
        "Coordinate Geometry": ["Cartesian System", "Plotting Points", "Graphing Lines"],
        "Trigonometry": ["Sin Cos Tan", "Trigonometric Identities", "Values Table"],
        "Surface Area and Volume": ["Cuboid", "Cylinder", "Cone", "Sphere"],

        "default": ["Key Definitions", "Real-life Examples", "Important Formulas", "Solved Problems"]
    }
}

# --- 3. DIAGRAM DATABASE ---
DIAGRAM_DB = {
    ("gravit", "newton", "force"): "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/NewtonsLawOfUniversalGravitation.svg/640px-NewtonsLawOfUniversalGravitation.svg.png",
    ("kepler", "orbit", "planet"): "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Kepler-first-law.svg/640px-Kepler-first-law.svg.png",
    ("periodic", "element", "table"): "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Periodic_Table_of_Elements_w_Name_and_Atomic_Number.svg/640px-Periodic_Table_of_Elements_w_Name_and_Atomic_Number.svg.png",
    ("atom", "electron", "structure"): "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Stylised_Lithium_Atom.svg/640px-Stylised_Lithium_Atom.svg.png",
    ("reaction", "chemical", "bond"): "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Chemical_reaction_of_methane_and_oxygen.svg/640px-Chemical_reaction_of_methane_and_oxygen.svg.png",
    ("current", "ohm", "circuit"): "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Ohm%27s_Law_with_Voltage_Source.svg/640px-Ohm%27s_Law_with_Voltage_Source.svg.png",
    ("motor", "generator", "magnetic"): "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Electric_motor_cycle_2.png/640px-Electric_motor_cycle_2.png",
    ("refract", "glass", "bending"): "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Snells_law2.svg/640px-Snells_law2.svg.png",
    ("lens", "convex", "concave"): "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Lens3.svg/640px-Lens3.svg.png",
    ("eye", "myopia", "vision"): "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Schematic_diagram_of_the_human_eye_en.svg/640px-Schematic_diagram_of_the_human_eye_en.svg.png",
    ("metallurgy", "blast furnace", "iron"): "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Blast_furnace_diagram.svg/450px-Blast_furnace_diagram.svg.png",
    ("carbon", "methane", "catenation"): "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Methane-2D-stereo.svg/640px-Methane-2D-stereo.svg.png",
    ("satellite", "space", "mission"): "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_Earth_Science_Enterprise_Spacecraft_Fleet_%282003%29.jpg/640px-NASA_Earth_Science_Enterprise_Spacecraft_Fleet_%282003%29.jpg",
    ("dna", "rna", "gene"): "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/DNA_Overview.png/400px-DNA_Overview.png",
    ("mitosis", "meiosis", "cell div"): "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Major_events_in_mitosis.svg/640px-Major_events_in_mitosis.svg.png",
    ("flower", "hibiscus", "reproduc"): "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Mature_flower_diagram.svg/640px-Mature_flower_diagram.svg.png",
    ("menstrual", "cycle", "female"): "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/MenstrualCycle_en.svg/580px-MenstrualCycle_en.svg.png",
    ("digest", "stomach", "system"): "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Digestive_system_diagram_en.svg/428px-Digestive_system_diagram_en.svg.png",
    ("heart", "blood", "circulat"): "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Diagram_of_the_human_heart_%28cropped%29.svg/640px-Diagram_of_the_human_heart_%28cropped%29.svg.png",
    ("brain", "neuron", "nervous"): "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Neuron_%28text%29.png/640px-Neuron_%28text%29.png",
    ("hydro", "dam", "water power"): "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Hydroelectric_dam.svg/640px-Hydroelectric_dam.svg.png",
    ("wind", "turbine", "mill"): "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Wind_turbine_diagram.svg/640px-Wind_turbine_diagram.svg.png",
    ("microbio", "bacteria", "ferment"): "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/EscherichiaColi_NIAID.jpg/640px-EscherichiaColi_NIAID.jpg",
    ("cell", "plant", "animal"): "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Animal_Cell.svg/640px-Animal_Cell.svg.png",
    ("motion", "newton", "law"): "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Newton%27s_cradle_animation_book_2.gif/300px-Newton%27s_cradle_animation_book_2.gif",
    ("plant", "kingdom", "classifi"): "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Plant_Diversity_updated.png/640px-Plant_Diversity_updated.png",
    ("ecosystem", "food chain", "web"): "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Trophic_Web.jpg/540px-Trophic_Web.jpg"
}