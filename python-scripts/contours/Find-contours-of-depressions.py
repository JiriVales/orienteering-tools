##Find contours of depressions=name
##numbermetersofenlargethedepressionarea=number9.0
##contours=vector
##dem=raster
##contoursofdepressions=output vector
outputs_MODELERFIND-DEPRESSION-AREA_1=processing.runalg('modeler:find-depression-area', dem,None)
outputs_QGISFIELDCALCULATOR_2=processing.runalg('qgis:fieldcalculator', contours,'depress',1,1.0,0.0,True,'0',None)
outputs_QGISPOLYGONSTOLINES_1=processing.runalg('qgis:polygonstolines', outputs_MODELERFIND-DEPRESSION-AREA_1['OUTPUT_ALGQGISEXTRACTBYATTRIBUTE_1'],None)
outputs_QGISFIXEDDISTANCEBUFFER_1=processing.runalg('qgis:fixeddistancebuffer', outputs_QGISPOLYGONSTOLINES_1['OUTPUT'],numbermetersofenlargethedepressionarea,5.0,False,None)
outputs_QGISMERGEVECTORLAYERS_1=processing.runalg('qgis:mergevectorlayers', [outputs_MODELERFIND-DEPRESSION-AREA_1['OUTPUT_ALGQGISEXTRACTBYATTRIBUTE_1'],outputs_QGISFIXEDDISTANCEBUFFER_1['OUTPUT']],None)
outputs_QGISDISSOLVE_1=processing.runalg('qgis:dissolve', outputs_QGISMERGEVECTORLAYERS_1['OUTPUT'],True,None,None)
outputs_QGISSELECTBYLOCATION_1=processing.runalg('qgis:selectbylocation', contours,outputs_QGISDISSOLVE_1['OUTPUT'],['within'],0.0,0)
outputs_QGISFIELDCALCULATOR_1=processing.runalg('qgis:fieldcalculator', outputs_QGISSELECTBYLOCATION_1['OUTPUT'],'depress',1,1.0,0.0,True,'1',None)
outputs_QGISMERGEVECTORLAYERS_2=processing.runalg('qgis:mergevectorlayers', [outputs_QGISFIELDCALCULATOR_1['OUTPUT_LAYER'],outputs_QGISFIELDCALCULATOR_2['OUTPUT_LAYER']],None)
outputs_QGISDELETEDUPLICATEGEOMETRIES_1=processing.runalg('qgis:deleteduplicategeometries', outputs_QGISMERGEVECTORLAYERS_2['OUTPUT'],contoursofdepressions)