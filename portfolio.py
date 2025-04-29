import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="El hadji Babou Portfolio",
    page_icon="🧩",
    layout="wide"
)

# Titre principal
st.title("El hadji Babou SEYE ")
st.markdown("# :blue-badge[Ingénieur en IA 🧩] | :red-badge[e.b.seye@gmail.com 📧] | :gray-badge[www.linkedin.com/in/el-hadji-babou-seye-128791281]")


# Section À propos
st.subheader("✨ À propos de moi ✨", divider="red")
st.markdown('''
Je suis passionné par l'informatique, plus particulièrement par l'IA.  
J'adore relever des défis et travailler sur des projets innovants qui ont un impact réel.
''')

# Section Cursus
st.subheader("🎓 Cursus académique 🎓", divider="red")
st.markdown('''
- **Master Chef de projet IA, Data Science** (2024–présent) à IA School Paris  
  _Focus_ : Management, Business, Gestion de projet, Data Science
- **Master Recherche en IA & ML** (2022–2024) co-accrédité Aix-Marseille Université / École Centrale Marseille  
  _Focus_ : Machine Learning, Deep Learning, Algèbre linéaire/bilinéaire, CNN, GAN, VAE, RNN (GRU, LSTM), Transformers, Recherche opérationnelle
- **Licence Informatique** (2019–2022) à Aix-Marseille Université  
  _Focus_ : Génie logiciel, Réseaux, Compilation, Architecture des ordinateurs, Statistiques, Probabilités

''')


# Section Compétences
st.subheader("🔧 Compétences clés 🔧", divider="red")
# Organiser les badges en colonnes
row1, row2, row3 = st.columns(3)
with row1:
    st.badge("NLP", icon="🗣️", color="green")
    st.badge("RAG", icon="📚", color="green")
    st.badge("Transfer Learning", icon="🔄", color="green")
with row2:
    st.badge("Reinforcement Learning", icon="🚀", color="green")
    st.badge("Deep Learning", icon="🧠", color="green")
    st.badge("Machine Learning", icon="📈", color="green")
with row3:
    st.badge("Agent IA", icon="🤖", color="green")
    st.badge("Finetuning", icon="🔧", color="green")
    st.badge("Stats & Data Analysis", icon="📊", color="green")


# Section Expériences
st.subheader("💼 Expériences professionnelles 💼", divider="red")

exp_col1, exp_col2 , exp_col3 = st.columns(3)
with exp_col3:
    st.markdown('''
    
**LIS-CNRS** – Marseille  
*Machine Learning / NLP Engineer* (Mai – Août 2023, stage)
- État de l’art sur coréférences textuelles
- Finetuning de LSTM pour résolution de coréférences

'''
)

with exp_col2:
    st.markdown('''**LIS-CNRS** – Marseille  
*Ingénieur IA/ML R&D* (Avr. – Sept. 2024, stage)
- Extraction de features audiovisuelles (OpenSmile, OpenFace)
- Nettoyage et préparation des données
- Création et validation de modèles (classification)
- Interprétabilité des modèles''')


with exp_col1:
    st.markdown('''
    
**IDEMIA FRANCE SAS** – Paris La Défense  
*Ingénieur IA générative & Deep Learning* (Déc. 2024–présent, alternance)
- R&D de solutions d’IA génératives pour l’industrie
- Analyse et traitement de données
- Évaluation, interprétation des résultats
- Déploiement en production
''')



# Section Environnement technique
st.subheader("💻 Environnement technique 💻", divider="red")
col1, col2, col3 = st.columns(3)
with col1:
    st.badge("Langages", icon="📝", color="green")
    st.markdown("- Python | Java | JavaScript")
    st.badge("Frameworks DL", icon="🛠️", color="green")
    st.markdown("- PyTorch | TensorFlow | Langchain (chatbot, Agent IA etc.)")
with col2:
    st.badge("ML", icon="🤖", color="green")
    st.markdown("- Scikit-Learn")
    st.badge("Data", icon="📊", color="green")
    st.markdown("- Pandas | NumPy")
with col3:
    st.badge("Visualisation", icon="📈", color="green")
    st.markdown("- Matplotlib | Seaborn")
    st.badge("Bases", icon="🗄️", color="green")
    st.markdown("- Redis | MySQL | MongoDB | PostgreSQL")

# # Section Projets réalisés
st.subheader("🚀 Projets réalisés", divider="red")
col1, col2, col3 = st.columns(3)

with col1:
    with col1:
        st.markdown('''
        ##### :green[Système de recherche de documents avec chatbot RAG intégré]
        **Contexte** : Les ingénieurs d'IDEMIA consacrent un temps important à la recherche d'informations dans les supports documentaires des outils utilisés.\n  
        **Objectif** : Améliorer l'accès à l'information et accroître la productivité des équipes.  \n
        **Solution** : Mise en place d'un **retriever** combinant BM25 (recherche lexicale) et BERT (recherche sémantique) pour identifier les passages pertinents.  
        Ces résultats alimentent un **générateur** LLaMA‑3.2‑3B (quantifié INT4) pour fournir des réponses contextualisées.  \n
        **Technologies** : `Redis` (gestion de l'historique et des sessions), `LangChain` (orchestration du pipeline RAG), `Streamlit` (interface et gestion des sessions), `FastAPI` + `Uvicorn` (scalabilité), `Docker` (conteneurisation, déploiement on-premise), `spaCy` (prétraitement et nettoyage des documents).
        ''')

    # Deuxième projet
    with col2:
        st.markdown('''
        ##### :green[Co-références pour la génération de questions NLP]
        **Contexte** : Exploration d'archives culturelles et patrimoniales nécessitant la compréhension des coréférences pour générer des questions pertinentes.  \n
        **Objectif** : Améliorer la génération automatique de questions en résolvant les coréférences au sein des textes.  \n
        **Solution** : Développement et évaluation d'un modèle de résolution de coréférences basé sur le Deep Learning (end-to-end), prendre en entrée du texte au format CONLL-U et produire des clusters de coréférences pour enrichir un pipeline de génération de questions.  \n
        **Technologies** : `spaCy` (prétraitement linguistique), `PyTorch` (implémentation du réseau LSTM et modèles end-to-end), `Hugging Face` (finetuning de modèles multilingues), `FastAPI` (API de service), `Docker` (conteneurisation).
        ''')

    # Troisième projet
    with col3:
        st.markdown('''
        ##### :green[Classification des attitudes sociales à partir de données temporelles]
        **Contexte** : Analyse de 30 fichiers CSV issus de scènes de confrontations pour détecter les attitudes sociales (colère chaude, colère froide, conciliante). Chaque fichier contient des vecteurs de grande dimension (334 features) enregistrés à 0.04 s d'intervalle.  \n
        **Objectif** : Construire des modèles de classification robustes pour prédire l'attitude sociale d'un enregistrement, et évaluer la performance à la fois au niveau des exemples et au niveau des fichiers.  \n
        **Solution** :
        - Prétraitement : vérification de la dimensionnalité, normalisation et labellisation par fichier (chaque fichier reçoit une étiquette unique).  
        - Séparation Train/Test par fichier pour éviter les fuites de données entre partitions.  
        - Entraînement et comparaison de plusieurs modèles de classification (SVM, forêts aléatoires, réseaux de neurones).  
        - Évaluation duale : précision par vecteur et par fichier (étiquette majoritaire).
        - Interprétabilité des features : Analyse de l'importance de chaque features selon les attitudes sociales avec les valeurs de chapley.\n 
        **Technologies** : `Pandas` et `NumPy` (préparation des données), `Scikit-Learn` (modèles de classification), `Matplotlib` / `Seaborn` (visualisation des distributions), `Docker` (conteneurisation).  
        ''')

st.markdown('''##### *:green[Précision] : J'ai travaillé sur d'autres project comme :gray-badge[la reconnaissance faciale] , :gray-badge[des agents IA (avec langchain)] , :gray-badge[la détection d'objets] sur des images ...*''')
# Pied de page
st.markdown('---')
st.markdown('© 2025 — Mon Portfolio IA')
