from django.db import models
import os


class imagens(models.Model):
    idImagens = models.AutoField(db_column='idCertificacao', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=45, blank=True, null=True)
    foto = models.ImageField()

    def __str__(self):
        return self.descricao

