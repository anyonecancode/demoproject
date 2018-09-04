#data/openbeerdb_csv.zip:
#	wget -O data/openbeerdb_csv.zip  openbeerdb.com/files/openbeerdb_csv.zip

#data/openbeerdb_csv:data/openbeerdb_csv.zip
#	unzip -d data data/openbeerdb_csv.zip

#data/beers.cleaned.csv:data/openbeerdb_csv
#	 tr -d '\n' < data/openbeerdb_csv/beers.csv | perl -pe  's/,{8,}/\n/g' > data/beers.cleaned.csv
SQL=data/beers.sql data/breweries.sql data/styles.sql data/categories.sql data/geocodes.sql

data/beers.sql:data/beers.zip
	unzip -j -o $< beers/beers.sql -d data
data/beers.zip:
	wget -O data/beers.zip  openbeerdb.com/files/beers.zip

data/breweries.sql:data/breweries.zip
	unzip -j -o $< breweries/breweries.sql -d data
data/breweries.zip:
	wget -O data/breweries.zip  openbeerdb.com/files/breweries.zip

data/styles.sql:data/cat_styles.zip
	unzip -j -o $< cat_styles/styles.sql -d data
data/categories.sql:data/cat_styles.zip
	unzip -j -o $< cat_styles/categories.sql -d data
data/cat_styles.zip:
	wget -O data/cat_styles.zip  openbeerdb.com/files/cat_styles.zip

data/geocodes.sql:data/geocodes.zip
	unzip -j -o $< geocodes/geocodes.sql -d data
data/geocodes.zip:
	wget -O data/geocodes.zip  openbeerdb.com/files/geocodes.zip

all: $(SQL)
