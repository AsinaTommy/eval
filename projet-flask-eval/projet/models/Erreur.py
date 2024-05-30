class Erreur:
    
    def __init__(self, message, ligne=None, colonne=None):
        self.ligne = ligne
        self.colonne = colonne
        self.message = message
    
    def json(self):
        return{'message': self.message, 'ligne': self.ligne, 'colonne': self.colonne}
        
        
        