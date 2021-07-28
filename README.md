# A/B Testing

![1_2Esr1uCL-6xwDBb5sCchmA@2x](https://user-images.githubusercontent.com/76595310/127244368-3e3d0974-8255-49a8-bccb-d5f10216bf94.jpeg)

## What is problem?

* A company wants to test a new feature on the website. 

* They want to determine which feature is useful for them or not by doing an A/B test.

## Story of data

* The dataset contains the information of the website. There is information such as the number of advertisements that users see and click, as well as earnings information from here.

* There are two separate data sets, control and test groups.

## Variables

* Impression: View count

* Click: Indicates the number of clicks on the displayed ad.

* Purchase: Indicates the number of products purchased after the ads clicked.

* Earning: Earnings after purchased products.

## About Project

In this project we will focus on purchases.

Assumptions must be checked first when making an A/B test. If the assumptions are provided, the t-test can be performed, if not non-parametric test is required.

After doing our A/B test, we see that there is no difference in terms of purchases, as you can see in the codes.

* So how can we decide which option will be better?

In which case we'll have to dig through the data a little more.

Let's look at the time of forty periods in terms of all features.

![grafikler](https://user-images.githubusercontent.com/76595310/127241423-4e7d3211-78c7-43cf-b0cc-05ca922dcb57.png)


The blue lines represent the test set and the orange lines the control set.

It seems like no difference except earning graph, one of them goes up other one goes down.  

Okey let's see total graphs and decide.

![graf](https://user-images.githubusercontent.com/76595310/127242163-3874ce08-e451-4c56-9bcc-2096a29a1c1d.png)

In this graph, you can see the total metrics for the test and control data.

If you look at the impression graph, there is a lot of difference, but somehow despite this difference, the control set is clearly ahead in click-through rates. This is like a discrepancy.
This observation gives me the impression that no two ads are the same and also that the ad for the test set isn't good because the difference in the ratio between the number of people who hit the ad and the number of clicks is huge 
and i saw that with a ratio test.

Therefore, there are several answers to the question of which choice will be better.

#### Conclusions

* First, the experiment can be continued because we did not observe any difference on our main metric.

* if we were to choose one, we might prefer the test, provided that the advertisement of the test set changes. If we get more people to click on this ad, there can be a noticeable difference in future purchases as well.



