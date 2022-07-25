#

# Project II Pipeline
## Web Scrapping for NFL players rankings
### By: Edgard Cuadra
### Date: July 25th 2022

#
![local_picture](./Images/Toprank.jpg)
#
## Hypothesis:
#

Use the 3 diferent experts ratings for top ranked players and add their overall rating stats to select the best player to draft within a budget cap. can we select the best posible draft out of this corrolation?
#

### Lets try and avoid dropping the ball!
<br/>

<p align="center">
  <img width="500" height="400" src= ./Images/giphy.gif
</p>
<br/>

#
## Data Cleaning:
#
First we find the webpage we want to get the information from so that we can scrape the data out of it. to make it legible we transform in into html format by using beutifulsoup.
<br/>

"https://www.cbssports.com/fantasy/football/rankings/"
<br/>
<p align="center">
  <img width="700" height="300" src= ./Images/Web_scarpe_page.jpg
</p>
<br/>

once we get the content in a format we can use we can proceed to extract the information wanted, in this cases we need player name, team, position and ranking. Now that we have extracted the information into separate lists we need to converge them into a dictionary in order for us to be able to turn it into a dataframe.
<br/>
Getting as a result:

![local_picture](./Images/table_rankings.jpg)

The web page pulled all the rankings into one dataframe, we need proceed to great 3 dataframes with the rankings. using iloc we are going to cut the dataframe into 3 tables and after merge them with the name index. we did this by using the next code:

    eisenbergranking = allrankings.iloc[0:200,:].reset_index(drop=True)
    richardranking = allrankings.iloc[200:400,:].reset_index(drop=True)
    cummingsranking = allrankings.iloc[400:600,:].reset_index(drop=True)

    x = [eisenbergranking, richardranking, cummingsranking]

    test = reduce(lambda left,right: pd.merge(left,
    right,on=['Player',"Position","Team"],how='outer'), x)

This gave us a table more sutable for our use:

![local_picture](./Images/table_rankings2.jpg)

From here on we did some minor ajustments and proceeded to make a calculated column with the average ranking and also renamed our columns to make it more readable.

![local_picture](./Images/table_rankings3.jpg)

Now that we have a usable table lets import the table wit the players stats that will help us determine the abilities every player excels with. this data base is being imported from kaggle and contains usefull information for all the players including salary.
<br/>

The table we imported has too much information that we dont need so we will drop the columns that are of no use to us, we can use the following code to eliminate by column position and make it easier and faster for us to drop the columns.
<br/> 

Used the following code to drop specific columns:

    nfl_stat2 = nfl_stat.drop(nfl_stat.columns[[11,12,13,14,15,16,17,20,21,22,23,24,25,26,28,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,62,63]], axis=1) 
<br/> 
In order to merge the two tables by thei identifying names we will have to use the same nomenclatures, thus the best approach would be to break into two columns and rearrange to get the desired initial and last name format.
<br/> 

Used the following code to get the correct format to merge both tables:

    nfl_stat2['lastname'] = nfl_stat2['Full Name'].str.split(' ', expand=True)[1]
    nfl_stat2['initials_'] =nfl_stat2['Full Name'].str.split('', expand=True)[1]
    nfl_stat2['short_name'] =  nfl_stat2['initials_']+ '. ' + nfl_stat2['lastname']

In order to merge both tables we need a bridge to tie the name with the nick name of the team, so we proceed to import another table that will help us get the missing piece of the puzzel and complete the tables before me merge them.
<br/> 

![local_picture](./Images/table_rankings5.jpg)

Now that we are certain that theres a match between this column its time to concatinate the tables, we want a inner cause we want to bring only the informarion of the top players and not all the 2500 players in the NFL league

We used the following code to make concat with a inner join, making it so that we keep only the information that there is a match where our top rank players receive the columns with all the stats of the ratings table

    toprank_stats = pd.concat([topranked2, final3], axis=1, join='inner')

Our final product is a table with all the information together and ready for visualization. 

Sample of the table:

![local_picture](./Images/table_rankings6.jpg)

#

Lets Get Started with the Visuals!
<p align="center">
  <img width="500" height="300" src= ./images/football-fail.gif
</p>


#
## Visualization and Storytelling:
#



#
## Conclusion and Recomendations:
#

<p align="center">
  <img width="500" height="300" src= ./images/football-dance.gif
</p>



create line break:
1.Surfing<br/>

make bold:
**Swimming**: