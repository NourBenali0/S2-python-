import tkinter as tk
import random
import string

# Fonction pour créer une clé de substitution (remplace chaque lettre par une autre)
def generer_clef_substitution():
    alphabet = list(string.ascii_lowercase)  # Liste des lettres de l'alphabet
    melange = alphabet[:]  # Copie de l'alphabet
    random.shuffle(melange)  # On mélange les lettres au hasard
    return dict(zip(alphabet, melange))  # On associe chaque lettre à une autre

# Fonction pour chiffrer un texte (remplace les lettres selon la clé)
def substitution_chiffrer(texte, clef):
    texte_chiffre = ""  # Chaîne vide pour stocker le résultat
    for lettre in texte.lower():  # On convertit en minuscules et on parcourt chaque lettre
        if lettre in clef:  # Si la lettre est dans la clé
            texte_chiffre += clef[lettre]  # On remplace par la lettre chiffrée
        else:
            texte_chiffre += lettre  # Sinon, on garde la lettre d'origine
    return texte_chiffre

# Fonction pour déchiffrer un texte (inverse le chiffrement)
def substitution_dechiffrer(texte_chiffre, clef):
    clef_inverse = {v: k for k, v in clef.items()}  # On inverse la clé
    texte_dechiffre = ""  # Chaîne vide pour stocker le texte déchiffré
    for lettre in texte_chiffre:
        if lettre in clef_inverse:
            texte_dechiffre += clef_inverse[lettre]  # Remplace par la lettre originale
        else:
            texte_dechiffre += lettre
    return texte_dechiffre

# Fonction appelée quand on clique sur le bouton
def rechercher():
    texte = entree.get()  # Récupère le texte entré par l'utilisateur
    
    if texte:  # Si l'utilisateur a tapé quelque chose
        clef = generer_clef_substitution()  # On génère une clé secrète
        texte_chiffre = substitution_chiffrer(texte, clef)  # On chiffre le texte
        texte_dechiffre = substitution_dechiffrer(texte_chiffre, clef)  # On déchiffre
        
        # On affiche les résultats
        resultat_label.config(text=f"Texte chiffré : {texte_chiffre}")
        decrypted_label.config(text=f"Texte déchiffré : {texte_dechiffre}")
    else:
        resultat_label.config(text="Veuillez entrer un texte.")  # Message d'erreur

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Chiffrement simple")
fenetre.geometry("400x250")

# Zone pour taper du texte
entree = tk.Entry(fenetre, width=40)
entree.pack(pady=10)

# Bouton pour chiffrer
bouton = tk.Button(fenetre, text="Chiffrer", command=rechercher)
bouton.pack(pady=5)

# Zone d'affichage des résultats
resultat_label = tk.Label(fenetre, text="", wraplength=350)
resultat_label.pack(pady=5)

decrypted_label = tk.Label(fenetre, text="", wraplength=350)
decrypted_label.pack(pady=5)

# Démarrer l'application Tkinter
fenetre.mainloop()
#exemple de chatgpt 











