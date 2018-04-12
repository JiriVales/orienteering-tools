##Create pits =name
##contoursofdepression=vector
##dem=raster
##pits=output vector
outputs_QGISLINESTOPOLYGONS_1=processing.runalg('qgis:linestopolygons', contoursofdepression,None)
outputs_MODELERFIND-DEPRESSION-AREA_1=processing.runalg('modeler:find-depression-area', dem,None)
outputs_QGISFIELDCALCULATOR_1=processing.runalg('qgis:fieldcalculator', outputs_MODELERFIND-DEPRESSION-AREA_1['OUTPUT_ALGQGISEXTRACTBYATTRIBUTE_1'],'area',0,10.0,1.0,True,'$area',None)
outputs_QGISEXTRACTBYATTRIBUTE_2=processing.runalg('qgis:extractbyattribute', outputs_QGISFIELDCALCULATOR_1['OUTPUT_LAYER'],'area',2,'4',None)
outputs_QGISEXTRACTBYLOCATION_1=processing.runalg('qgis:extractbylocation', outputs_QGISEXTRACTBYATTRIBUTE_2['OUTPUT'],outputs_QGISLINESTOPOLYGONS_1['OUTPUT'],['intersects'],0.0,None)
outputs_QGISFIELDCALCULATOR_3=processing.runalg('qgis:fieldcalculator', outputs_QGISEXTRACTBYLOCATION_1['OUTPUT'],'isdepres',1,1.0,0.0,True,'1',None)
outputs_QGISFIELDCALCULATOR_4=processing.runalg('qgis:fieldcalculator', outputs_QGISEXTRACTBYATTRIBUTE_2['OUTPUT'],'isdepres',1,1.0,0.0,True,'0',None)
outputs_QGISMERGEVECTORLAYERS_1=processing.runalg('qgis:mergevectorlayers', [outputs_QGISFIELDCALCULATOR_3['OUTPUT_LAYER'],outputs_QGISFIELDCALCULATOR_4['OUTPUT_LAYER']],None)
outputs_QGISDELETEDUPLICATEGEOMETRIES_1=processing.runalg('qgis:deleteduplicategeometries', outputs_QGISMERGEVECTORLAYERS_1['OUTPUT'],None)
outputs_QGISEXTRACTBYATTRIBUTE_5=processing.runalg('qgis:extractbyattribute', outputs_QGISDELETEDUPLICATEGEOMETRIES_1['OUTPUT'],'isdepres',0,'0',None)
outputs_QGISEXTRACTBYATTRIBUTE_4=processing.runalg('qgis:extractbyattribute', outputs_QGISEXTRACTBYATTRIBUTE_5['OUTPUT'],'area',4,'137',None)
outputs_SAGAPOLYGONCENTROIDS_1=processing.runalg('saga:polygoncentroids', outputs_QGISEXTRACTBYATTRIBUTE_4['OUTPUT'],True,pits)