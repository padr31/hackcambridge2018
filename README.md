# Impressio

This app was developed in 24 hours at the [Hack Cambridge 2018](https://hackcambridge.com/) hackathon.

Impressio estimates engagement and amusement of an audience from a real-time camera stream.

<img src="/screenshots/screenshot1.jpg?raw=true" alt="Cover image"/>

**Authors:**

- Pavol Drotár ([padr31](https://github.com/padr31))
- Juraj Mičko ([jjurm](https://github.com/jjurm))
- Michal Pándy ([mpmisko](https://github.com/mpmisko))
- Marko Puza ([markopuza](https://github.com/markopuza))
- Martin Ferianc ([fexter-svk](https://github.com/fexter-svk))

## Inspiration

In order to make an impactful presentation audience engagement is crucial. Currently, there are little to no tools that would aid presenters in their endeavour to communicate their ideas in an amusing and witty way. We wanted to create a tool that would show presenters live data about how the audience is feeling about their presentation. This way they could not only adjust thier delivery in the moment, but also go over their performance after the presentation.

## What it does

Our solution uses the phone's camera to continuously capture images of the audience during a presentation or a talk. We try to recognise human faces in the image and estimate their emotions. Based on that, our algorithm tells how engaged and amused the audience is.

Once we have the real time data about the amusement of the audience, we can utilise it in many ways. The presenter's dashboard offers simple evaluation of their performance on the stage, visualisation of the measured values over time in nice charts, histogram of different emotions present in the audience as well as a short motivative quote to encourage the presenter.

After the presentation, the data taken can be analysed and matched with the presenter's slides to gauge how well the slides were designed.

## How we built it

We have a backend in Python that connects to and send pictures to the Microsoft Cognitive API. The backend then processes the output of the API so that we can get the final 'amusement' of the audience. Then we have a frontend in Angular 2 that displays a dashboard with real time data from the backend - current amusement, histogram of different emotions, long term amusement, overall feeling, and also provides useful suggestions for people who are presenting.

## Challenges we ran into

Perhaps the greatest challenge was making the data extracted from the Emotions API useful for the presenter. We wanted to make sure that we don't only show a bunch of graphs, but that what we provide has real meaning for people delivering the presentation. We had to give a lot of thought into this aspect of our project.

## Accomplishments that we're proud of

We are proud that we were able to overcome various technical challenges throughout the hackathon and create a functional prototype of Impressio - using technologies that most of us were not familiar with.

## What we learned

We explored the abilities of the state-of-art face recognition API, learned to build a multithreaded backend server in Python and frontend in Angular. Another useful skill is certainly learning how to control the camera of a smartphone remotely.

## What's next for Impressio

There are vast applications of the project which we think have a great potential to explore. One of these could be putting Impressio to cinemas to monitor people's emotions and this way automate movie feedback. Or, Impressio could replace surveys that companies make for customers when testing a new product. We would definitely like to explore more applications of our product in the future.
