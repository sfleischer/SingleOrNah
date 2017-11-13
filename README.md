# SingleOrNah
Ever wonder if that one cutie is single? Simply input their Insta handle and get a prediction back in seconds!

## Inspiration

We're computer science students, need we say more?

## What it does

"Single or Nah" takes in the name of a friend and predicts if they are in a relationship, saving you much time (and face) in asking around.  We pull relevant Instagram data including posts, captions, and comments to drive our Azure-powered analysis.  Posts are analyzed for genders, ages, emotions, and smiles -- with each aspect contributing to the final score.  Captions and comments are analyzed for their sentiment, which give insights into one's relationship status.  Our final product is a hosted web-app that takes in a friend's Instagram handle and generate a percentage denoting how likely they are to be in a relationship.

## How we built it

Our first problem was obtaining Instagram data.  The tool we use is a significantly improved version of an open-source Instagram scraper API (https://github.com/rarcega/instagram-scraper).  The tool originally ran as a Python command line argument, which was impractical to use in a WebApp.  We modernized the tool, giving us increased flexibility and allowing us to use it within a Python application.

We run Microsoft's Face-API on the target friend's profile picture to guess their gender and age -- this will be the age range we are interested in.  Then, we run through their most recent posts, using Face-API to capture genders, ages, emotions, and smiles of people in those posts to finally derive a sub-score that will factor into the final result.  We guess that the more happy and more pictures with the opposite gender, you'd be less likely to be single!

We take a similar approach to captions and comments.  First, we used Google's Word2vec to generate semantically similar words to certain keywords (love, boyfriend, girlfriend, relationship, etc.) as well as assign weights to those words.  Furthermore, we included Emojis (😍😍 is usually a good giveaway!) into our weighting scheme[link](https://gist.github.com/chrisfischer/144191eae03e64dc9494a2967241673a).  We use Microsoft's Text Analytics API on this keywords-weight scheme to obtain a sentiment sub-score and a keyword sub-score.

Once we have these sub-scores, we aggregate them into a final percentage, denoting how likely your friend is single.  It was time to take it live.  We integrated all the individual calculations and aggregations into a Django., then hosted all necessary computation using Azure WebApps.  Finally, we designed a simple interface to allow inputs as well as to display results with a combination of HTML, CSS, JavaScript, and JQuery.

## Challenges I ran into

The main challenge was that we were limited by our resources. We only had access to basic accounts for some of the software we used, so we had to be careful how on often and how intensely we used tools to prevent exhausting our subscriptions.  For example, we limited the number of posts we analyzed per person.  Also, our Azure server uses the most basic service, meaning it does not have enough computing power to host more than a few clients.

The application only works on "public" Instagram ideas, so we were unable to find a good number of test subjects to fine tune our process.  For the accounts we did have access to, the application produced a reasonable answer, leading us to believe that the app is a good predictor.

## Accomplishments that we're proud of

We proud that we were able to build this WebApp using tools and APIs that we haven't used before.  In the end, our project worked reasonably well and accurately.  We were able to try it on people and get a score which is an accomplishment in that.  Finally, we're proud that we were able to create a relevant tool in today's age of social media -- I mean I know I would use this app to narrow down who to DM.

## What we learned

We learned about the Microsoft Azure API (Face API, Text Analytics API, and web hosting), NLP techniques, and full stack web development.  We also learned a lot of useful software development techniques such as how to better use git to handle problems, creating virtual environments, as well as setting milestones to meet.

## What's next for Single or Nah

The next steps for Single or Nah is to make the website and computations more scalable.  More scalability allows more people to use our product to find who they should DM -- and who doesn't want that??  We also want to work on accuracy, either by adjusting weights given more data to learn from or by using full-fledged Machine Learning.  Hopefully more accuracy would save "Single or Nah" from some awkward moments... like asking someone out... who isn't single...
