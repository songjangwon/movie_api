
from rest_framework import serializers
from .models import Movie
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie # 모델 설정
        fields = ('id','title','genre','year') # 필드 설정

    # @detail_route(methods=['post'])
    # def run_analysis(self, request, pk):
    #     return "디져라"
        # stock_portfolio = get the object based on the pk
        # holdings = make your query to get the holdings
        # analysis_result = HoldingsAnalyser.run(holdings)
        # if analysis_result:
        #     # everything ok
        #     return Response(status=status.HTTP_204_NO_CONTENT)
        # else:
        #     return Response(a useful error for your client)