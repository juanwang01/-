from luffycityapi.luffycityapi.utils import constants,views
# from rest_framework.generics import ListAPIView
from .models import Nav, Banner
from .serializers import NavModelSerializer, BannerModelSerializer


class NavHeaderListAPIView(views.CacheListAPIView):
    """顶部导航视图"""
    queryset = Nav.objects.filter(position=constants.NAV_HEADER_POSITION, is_show=True, is_deleted=False).order_by(
        "orders", "-id")[:constants.NAV_HEADER_SIZE]
    serializer_class = NavModelSerializer


class NavFooterListAPIView(views.CacheListAPIView):
    """脚部导航视图"""
    queryset = Nav.objects.filter(position=constants.NAV_FOOTER_POSITION, is_show=True, is_deleted=False).order_by(
        "orders", "-id")[:constants.NAV_FOOTER_SIZE]
    serializer_class = NavModelSerializer


class BannerListAPIView(views.CacheListAPIView):
    """轮播广告视图"""
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")[:constants.BANNER_SIZE]
    serializer_class = BannerModelSerializer
