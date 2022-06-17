from random import choice
from django.db import models
from django.contrib.postgres.fields import ArrayField
 
class YPModel(models.Model):
    date = models.DateField(null=False, blank=False)
    category = models.TextField()
    sentence = models.TextField(null=False, blank=False)
    sentence_short = ArrayField(models.TextField(),default=list)
    sentence_keywords = ArrayField(ArrayField(models.TextField(blank=True),size=2),blank=True,default=list)
    sentence_sentiment = ArrayField(models.FloatField(),size=2,default=list)
    sentence_sentiment_net = models.FloatField()
    sentence_sent_score = models.FloatField()
    sentence_sentiment_label = models.IntegerField()
    sentence_entities =  ArrayField(ArrayField(models.TextField(),size=2),blank=True,default=list)
    sentence_non_entities = ArrayField(models.TextField(),blank=True,default=list)

    def __str__(self):
        return self.sentence

class GZModel(models.Model):
    date = models.DateField(null=False, blank=False)
    logits = models.FloatField(null=False, blank=False)
    net_sent = models.FloatField(null=False, blank=False)
    logits_mean = models.FloatField(null=False, blank=False)
    net_sent_mean = models.FloatField(null=False, blank=False)
    MA_logits = models.FloatField(null=False, blank=False)
    MA_net_sent = models.FloatField(null=False, blank=False)
    MA_net_sent_ema_alpha_0_1 = models.FloatField(null=False, blank=False)
    MA_net_sent_ema_alpha_0_3 = models.FloatField(null=False, blank=False)
    MA_net_sent_ema_alpha_0_5 = models.FloatField(null=False, blank=False)

    def __str__(self):
        return str(self.logits)