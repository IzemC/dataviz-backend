from .models import YPModel, GZModel
from rest_framework import serializers

class YPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YPModel
        fields = ('id', 'date' , 'category' , 'sentence' ,'sentence_short' , 'sentence_keywords' , 'sentence_sentiment', 'sentence_sentiment_net', 'sentence_sent_score' ,  'sentence_sentiment_label' ,'sentence_entities' , 'sentence_non_entities')

class GZSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GZModel
        fields = ('id', 'date', 'logits' , 'net_sent', 'logits_mean' ,'net_sent_mean' , 'MA_logits', 'MA_net_sent','MA_net_sent_ema_alpha_0_1','MA_net_sent_ema_alpha_0_3','MA_net_sent_ema_alpha_0_5' )