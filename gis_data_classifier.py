files = ['roads.shp', 'elevation.tif', 'population.csv']

print( "GIS data Report")

for file in files:
  print('--------------------------------')
  if file[-3:] == 'shp':
    print(file, 'is  vector data')
  elif file[-3:]  == 'tif':
    print(file,'is a raster data')
  elif file[-3:]   == 'csv':
   print(file,'is table data')
