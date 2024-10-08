"""
URL configuration for wat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from waterflow.views import (
    basic_details,
    source_water_profile,
    rainwater,
    delete_rainwater,
    fresh_water_treatment_profile,
    source_water_pie_chart,
    delete_fresh_water_treatment_profile,
    delete_basic_details,
    delete_source_water_profile,
    fresh_water_treatment_profile_details,
    source_water_flow,
    delete_source_water_flow,
    tanks_capacities,
    delete_tanks_capacities,
    kitchen_consumption_view,
    delete_kitchen_consumption,
    drinking_water_source_view,
    delete_drinking_water_source,
    restaurant_consumption_view,
    delete_restaurant_consumption,
    delete_restaurant,
    delete_kitchen,
    banquet_consumption_view,
    delete_banquet_consumption,
    delete_banquet,
    guestroom_consumption_view,
    delete_guestroom_consumption,
    delete_guestroom,
    employeeroom_consumption_view,
    delete_employeeroom_consumption,
    delete_employeeroom,
    driversroom_consumption_view,
    delete_driversroom_consumption,
    delete_driversroom,
    swimmingpool_consumption_view,
    delete_swimmingpool_consumption,
    waterbodies_consumption_view,
    delete_waterbodies_consumption,
    laundry_consumption_view,
    delete_laundry_consumption,
    boiler_consumption_view,
    delete_boiler_consumption,
    boiler_treatment_methods_view,
    delete_boiler_treatment_method,
    add_boiler_view,
    delete_each_boiler_consumption,
    delete_each_boiler,
    calorifier_consumption_view,
    delete_calorifier_consumption,
    delete_calorifier,
    coolingtower_consumption_view,
    delete_coolingtower_consumption,
    add_coolingtower_view,
    delete_each_coolingtower_consumption,
    delete_each_coolingtower,
    irrigation_consumption_view,
    delete_irrigation_consumption,
    other_consumption_view,
    delete_other_consumption,
    wastewater_treatment_view,
    wastewater_treatment_STP_view,
    wastewater_treatment_ETP_view,
    wastewater_treatment_Others_view,
    delete_wastewater_treatment_STP,
    delete_wastewater_treatment_ETP,
    delete_wastewater_treatment_Others,
    delete_wastewater_treatment,
    tanks_and_capacities_view,
    delete_tanks_and_capacities,
    water_quality_profile_view,
    delete_water_quality_profile,
    recycled_water_view,
    delete_recycled_water_all,
    delete_recycled_water,
)

urlpatterns = [
    path("", basic_details, name="basic_details"),
    path("delete-basic-details/", delete_basic_details, name="delete_basic_details"),
    path("source-water-profile/", source_water_profile, name="source_water_profile"),
    path("rainwater-details", rainwater, name="rainwater_details"),
    path("delete-rainwater", delete_rainwater, name="delete_rainwater"),
    path(
        "delete-source-water-profile",
        delete_source_water_profile,
        name="delete_source_water_profile",
    ),
    path(
        "fresh-water-treatment-profile/",
        fresh_water_treatment_profile,
        name="fresh_water_treatment_profile",
    ),
    path(
        "delete-fresh-water-treatment-profile/",
        delete_fresh_water_treatment_profile,
        name="delete_fresh_water_treatment_profile",
    ),
    path(
        "source-water-distribution/",
        source_water_pie_chart,
        name="source_water_distribution",
    ),
    path(
        "fresh-water-treatment-profile-details/",
        fresh_water_treatment_profile_details,
        name="fresh_water_treatment_profile_details",
    ),
    path("tanks-capacities/", tanks_capacities, name="tanks_capacities"),
    path(
        "delete-tanks-capacities/",
        delete_tanks_capacities,
        name="delete_tanks_capacities",
    ),
    path('sources-destinations/',source_water_flow, name='source_water_flow'),
    path('delete-tanks-capacities/',delete_source_water_flow, name='delete_source_water_flow'),
    path(
        "kitchen-consumption-view", kitchen_consumption_view, name="kitchen_consumption"
    ),
    path(
        "delete-kitchen-consumption",
        delete_kitchen_consumption,
        name="delete_kitchen_consumption",
    ),
    path("delete-kitchen/<int:kitchen_id>/", delete_kitchen, name="delete_kitchen"),
    path(
        "drinking-water-source",
        drinking_water_source_view,
        name="drinking_water_source",
    ),
    path(
        "delete-drinking-water-source",
        delete_drinking_water_source,
        name="delete_drinking_water",
    ),
    path(
        "restaurant-consumption-view",
        restaurant_consumption_view,
        name="restaurant_consumption",
    ),
    path(
        "delete-restaurant-consumption",
        delete_restaurant_consumption,
        name="delete_restaurant_consumption",
    ),
    path(
        "delete-restaurant/<int:restaurant_id>/",
        delete_restaurant,
        name="delete_restaurant",
    ),
    path(
        "banquet-consumption-view", banquet_consumption_view, name="banquet_consumption"
    ),
    path(
        "delete-banquet-consumption",
        delete_banquet_consumption,
        name="delete_banquet_consumption",
    ),
    path("delete-banquet/<int:banquet_id>/", delete_banquet, name="delete_banquet"),
    path(
        "guestroom-consumption-view",
        guestroom_consumption_view,
        name="guestroom_consumption",
    ),
    path(
        "delete-guestroom-consumption",
        delete_guestroom_consumption,
        name="delete_guestroom_consumption",
    ),
    path(
        "delete-guestroom/<int:guestroom_id>/",
        delete_guestroom,
        name="delete_guestroom",
    ),
    path(
        "employeeroom-consumption-view",
        employeeroom_consumption_view,
        name="employeeroom_consumption",
    ),
    path(
        "delete-employeeroom-consumption",
        delete_employeeroom_consumption,
        name="delete_employeeroom_consumption",
    ),
    path(
        "delete-employeeroom/<int:employeeroom_id>/",
        delete_employeeroom,
        name="delete_employeeroom",
    ),
    path(
        "driversroom-consumption-view",
        driversroom_consumption_view,
        name="driversroom_consumption",
    ),
    path(
        "delete-driversroom-consumption",
        delete_driversroom_consumption,
        name="delete_driversroom_consumption",
    ),
    path(
        "delete-driversroom/<int:driversroom_id>/",
        delete_driversroom,
        name="delete_driversroom",
    ),
    path(
        "swimmingpool-consumption-view",
        swimmingpool_consumption_view,
        name="swimmingpool_consumption",
    ),
    path(
        "delete-swimmingpool-consumption",
        delete_swimmingpool_consumption,
        name="delete_swimmingpool_consumption",
    ),
    path(
        "waterbodies-consumption-view",
        waterbodies_consumption_view,
        name="waterbodies_consumption",
    ),
    path(
        "delete-waterbodies-consumption",
        delete_waterbodies_consumption,
        name="delete_waterbodies_consumption",
    ),
    path(
        "laundry-consumption-view", laundry_consumption_view, name="laundry_consumption"
    ),
    path(
        "delete-laundry-consumption",
        delete_laundry_consumption,
        name="delete_laundry_consumption",
    ),
    path("boiler-consumption-view", boiler_consumption_view, name="boiler_consumption"),
    path(
        "delete-boiler-consumption",
        delete_boiler_consumption,
        name="delete_boiler_consumption",
    ),
    path(
        "boiler-treatment-method-view",
        boiler_treatment_methods_view,
        name="boiler_treatment_method",
    ),
    path(
        "delete-boiler-treatment-method/<int:boiler_treatment_id>/",
        delete_boiler_treatment_method,
        name="delete_boiler_treatment_method",
    ),
    path("add-boiler-view", add_boiler_view, name="add_boiler"),
    path(
        "delete-each-boiler-consumption",
        delete_each_boiler_consumption,
        name="delete_each_boiler_consumption",
    ),
    path(
        "delete-each-boiler/<int:boiler_id>/",
        delete_each_boiler,
        name="delete_each_boiler",
    ),
    path(
        "calorifier-consumption-view",
        calorifier_consumption_view,
        name="calorifier_consumption",
    ),
    path(
        "delete-calorifier-consumption",
        delete_calorifier_consumption,
        name="delete_calorifier_consumption",
    ),
    path(
        "delete-calorifier/<int:calorifier_id>/",
        delete_calorifier,
        name="delete_calorifier",
    ),
    path(
        "coolingtower-consumption-view",
        coolingtower_consumption_view,
        name="coolingtower_consumption",
    ),
    path(
        "delete-coolingtower-consumption",
        delete_coolingtower_consumption,
        name="delete_coolingtower_consumption",
    ),
    path("add-coolingtower-view", add_coolingtower_view, name="add_coolingtower"),
    path(
        "delete-each-coolingtower-consumption",
        delete_each_coolingtower_consumption,
        name="delete_each_coolingtower_consumption",
    ),
    path(
        "delete-each-coolingtower/<int:coolingtower_id>/",
        delete_each_coolingtower,
        name="delete_each_coolingtower",
    ),
    path(
        "irrigation-consumption-view",
        irrigation_consumption_view,
        name="irrigation_consumption",
    ),
    path(
        "delete-irrigation-consumption",
        delete_irrigation_consumption,
        name="delete_irrigation_consumption",
    ),
    path("other-consumption-view", other_consumption_view, name="other_consumption"),
    path(
        "delete-other-consumption",
        delete_other_consumption,
        name="delete_other_consumption",
    ),
    path(
        "wastewater-treatment-view",
        wastewater_treatment_view,
        name="wastewater_treatment",
    ),
    path(
        "delete-wastewater-treatment",
        delete_wastewater_treatment,
        name="delete_wastewater_treatment",
    ),
    path(
        "wastewater-treatment-STP-view",
        wastewater_treatment_STP_view,
        name="wastewater_treatment_STP",
    ),
    path(
        "delete-wastewater-treatment-STP",
        delete_wastewater_treatment_STP,
        name="delete_wastewater_treatment_STP",
    ),
    path(
        "wastewater-treatment-ETP-view",
        wastewater_treatment_ETP_view,
        name="wastewater_treatment_ETP",
    ),
    path(
        "delete-wastewater-treatment-ETP",
        delete_wastewater_treatment_ETP,
        name="delete_wastewater_treatment_ETP",
    ),
    path(
        "wastewater-treatment-Others-view",
        wastewater_treatment_Others_view,
        name="wastewater_treatment_Others",
    ),
    path(
        "delete-wastewater-treatment-others",
        delete_wastewater_treatment_Others,
        name="delete_wastewater_treatment_Others",
    ),
    path(
        "tanks-and-capacities-view",
        tanks_and_capacities_view,
        name="tanks_and_capacities",
    ),
    path(
        "delete-tanks-and-capacities",
        delete_tanks_and_capacities,
        name="delete_tanks_and_capacities",
    ),
    path(
        "water-quality-profile-view",
        water_quality_profile_view,
        name="water_quality_profile",
    ),
    path(
        "delete-water-quality-profile",
        delete_water_quality_profile,
        name="delete_water_quality_profile",
    ),

    path(
        "recycled-water-view", recycled_water_view, name="recycled_water"
    ),
    path(
        "delete-recycled-water",
        delete_recycled_water_all,
        name="delete_recycled_water_all",
    ),
    path("delete-recycled-water/<int:recycled_water_id>/", delete_recycled_water, name="delete_recycled_water"),
    
    
]
