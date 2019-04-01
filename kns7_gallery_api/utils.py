from datetime import datetime, date

class DicoMixin:

    @property
    def dico(self) -> dict:
        """
        Transforme un dict en dict serializable.
        Marche pour:
            *object datetime
            *object date
        Args:
            dico: le dict à transformer
        Returns:
            un nouveau dict.
        """
        new_dict = {}

        for k, v in self.to_dict().items():
            if isinstance(v, datetime):
                new_dict[k] = v.isoformat()

            elif isinstance(v, date):
                new_dict[k] = v.isoformat()
            else:
                new_dict[k] = v
        return new_dict