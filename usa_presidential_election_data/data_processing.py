import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder


def preprocess_usa_elections_data(df: pd.DataFrame) -> pd.DataFrame:
    
    # variables categoricas
    df['state_abbreviation'] = LabelEncoder().fit_transform(df['state_abbreviation'])
    df['county_name'] = LabelEncoder().fit_transform(df['county_name'])
    df['area_name'] = LabelEncoder().fit_transform(df['area_name'])
    
    # selección de variables
    df = df.drop(['Unnamed: 0', 'X', 'combined_fips', 'votes_dem_2016', 'votes_gop_2016',
                  'Clinton', 'diff_2016', 'state_abbr',
                  'per_point_diff_2016', 
                  'diff_2012', 'per_point_diff_2012',
                  'population_change', 'Clinton_Obama', 'Trump_Romney', 'Trump_Prediction',
                  'Clinton_Prediction', 'Trump_Deviation', 'Clinton_Deviation',
                 'total_votes_2012', 'votes_dem_2012', 'votes_gop_2012', 'Romney'], 1)
    
    return df

#############################################################
# FIELD DEFINITION
#############################################################
# code	desc
# PST045214	Population, 2014 estimate
# PST040210	Population, 2010 (April 1) estimates base
# PST120214	Population, percent change - April 1, 2010 to July 1, 2014
# POP010210	Population, 2010
# AGE135214	Persons under 5 years, percent, 2014
# AGE295214	Persons under 18 years, percent, 2014
# AGE775214	Persons 65 years and over, percent, 2014
# SEX255214	Female persons, percent, 2014
# RHI125214	White alone, percent, 2014
# RHI225214	Black or African American alone, percent, 2014
# RHI325214	American Indian and Alaska Native alone, percent, 2014
# RHI425214	Asian alone, percent, 2014
# RHI525214	Native Hawaiian and Other Pacific Islander alone, percent, 2014
# RHI625214	Two or More Races, percent, 2014
# RHI725214	Hispanic or Latino, percent, 2014
# RHI825214	White alone, not Hispanic or Latino, percent, 2014
# POP715213	Living in same house 1 year & over, percent, 2009-2013
# POP645213	Foreign born persons, percent, 2009-2013
# POP815213	Language other than English spoken at home, pct age 5+, 2009-2013
# EDU635213	High school graduate or higher, percent of persons age 25+, 2009-2013
# EDU685213	Bachelor's degree or higher, percent of persons age 25+, 2009-2013
# VET605213	Veterans, 2009-2013
# LFE305213	Mean travel time to work (minutes), workers age 16+, 2009-2013
# HSG010214	Housing units, 2014
# HSG445213	Homeownership rate, 2009-2013
# HSG096213	Housing units in multi-unit structures, percent, 2009-2013
# HSG495213	Median value of owner-occupied housing units, 2009-2013
# HSD410213	Households, 2009-2013
# HSD310213	Persons per household, 2009-2013
# INC910213	Per capita money income in past 12 months (2013 dollars), 2009-2013
# INC110213	Median household income, 2009-2013
# PVY020213	Persons below poverty level, percent, 2009-2013
# BZA010213	Private nonfarm establishments, 2013
# BZA110213	Private nonfarm employment, 2013
# BZA115213	Private nonfarm employment, percent change, 2012-2013
# NES010213	Nonemployer establishments, 2013
# SBO001207	Total number of firms, 2007
# SBO315207	Black-owned firms, percent, 2007
# SBO115207	American Indian- and Alaska Native-owned firms, percent, 2007
# SBO215207	Asian-owned firms, percent, 2007
# SBO515207	Native Hawaiian- and Other Pacific Islander-owned firms, percent, 2007
# SBO415207	Hispanic-owned firms, percent, 2007
# SBO015207	Women-owned firms, percent, 2007
# MAN450207	Manufacturers shipments, 2007 (1,000)
# 𝑊𝑇𝑁220207|𝑀𝑒𝑟𝑐ℎ𝑎𝑛𝑡𝑤ℎ𝑜𝑙𝑒𝑠𝑎𝑙𝑒𝑟𝑠𝑎𝑙𝑒𝑠,2007(1,000)
# WTN220207|Merchantwholesalersales,2007(1,000)
# RTN130207	Retail sales, 2007 (1,000)
# 𝑅𝑇𝑁131207|𝑅𝑒𝑡𝑎𝑖𝑙𝑠𝑎𝑙𝑒𝑠𝑝𝑒𝑟𝑐𝑎𝑝𝑖𝑡𝑎,2007
# 𝐴𝐹𝑁120207|𝐴𝑐𝑐𝑜𝑚𝑚𝑜𝑑𝑎𝑡𝑖𝑜𝑛𝑎𝑛𝑑𝑓𝑜𝑜𝑑𝑠𝑒𝑟𝑣𝑖𝑐𝑒𝑠𝑠𝑎𝑙𝑒𝑠,2007(1,000)
# RTN131207|Retailsalespercapita,2007
# AFN120207|Accommodationandfoodservicessales,2007(1,000)
# BPS030214	Building permits, 2014
# LND110210	Land area in square miles, 2010
# POP060210	Population per square mile, 2010