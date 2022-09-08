# On the diagnostics project

These instructions introduce your task for the next few weeks, working on the
project.  Specifically, these instructions are about the pull request (PR) that
contain these instructions, and how to get going on your analysis plan.

We should say to start off, that the term *analysis plan* is a bit grand.  It
should better be called an analysis sketch.

The purpose of this PR is:

1. Practice on some Git / Github collaboration *with us and with each other*.
2. Practice on editing [Markdown text](https://www.markdowntutorial.com).
3. Giving you a chance to ask us questions about the project.
4. Making sure you're ready to get going with improving code to detect
   outliers.
5. Giving you more information on your task.
6. Making a sketch of what you want to do over the next week or two for the
   project.

## Github practice, questions

You are going to get this file, and several others, as a *pull request* (PR) to
your repository.

Your first job is to use this PR to ask questions of us, your instructors.

What we propose you do, is use the PR interface to ask for clarification about
the task, or the project.  You can enter comments in the PR interface, or go
the "Files changed" tabs, and click on individual lines to add comments or
questions about specific lines in the file.

Use the tag `@nipraxis-fall-2022/instructors` to point us to your questions.

Once you are happy you've understood the task, merge this PR.

## On Markdown

The file is in Markdown format, and you will be writing an analysis plan, also
in Markdown.

Markdown is a *markup language*.  A Markdown file is a conventional text file
that you can open in any text editor.  The special aspect of a Markdown file is
the *markup*.   Markup consists of special bits of text that specify
*formatting* of the text.  For example, in order to make a word in **bold**
text, using Markdown markup, you put two asterisks either side of the text you
want to be in bold.  When you want a properly formatted version of your
Markdown file, you convert it to the formatted version, using a *Markdown
renderer*.  A Markdown renderer is some system that can interpret the Markdown
markup and display the text as you intended, with bold text as bold, headings
as headings and so on.

There are very many Markdown renderers, but the Github site is one.   When you
put a `.md` file into your repository, like this one, and then navigate to the
relevant file in the Github web interface, you will see that Github has
*rendered* the Markdown formatting, showing bold as **bold**, headings as
headings, and so on.

Markdown has become the standard way of writing text files with markup, and you
will see it everywhere on systems that programmers use, such as Github, and in
the Jupyter notebook.

Markdown has many dialects, meaning that there is some markup that every
Markdown renderer understands, such as **bold**, and other markup that only
some renderers understand.  The Markdown that every renderer understands is
called [standard Markdown](https://www.markdownguide.org/basic-syntax). Github
has its own dialect of Markdown, called [Github flavored
Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github).
You can usually stick to the standard stuff, but you may need to consult the
Github documents if you want to do something slightly more fancy, like a table.

## Making sure you're ready

To be ready to get going on your project you need to make sure you have merged these three PRs:

* "add-dvars"
* "Add machinery to install module directory."
* "Fix use of Path in find_outliers script"

Make sure you've done the exercises there.  Run the following checks, from the
homeworks:

```
# You should see no errors.
python3 scripts/validate_data.py
```

```
# You should see: "Tests passed".
python3 findoutlie/tests/test_detectors.py
```

```
# You should see "=== ? passed in ? seconds ==="
# Where ? are numbers that will depend on your system and repository.
pytest findoutlie
```

If you don't get these outputs, check back with us by tagging use with a
question on this PR.

Next, have a look at the `findoutlie/outfind.py` *in this PR*.  You will see a
basic implementation of outlier detection using your DVARs implementation, from
the homework.

*After you have merged this PR*, you can run:

```
python3 scripts/find_outliers.py data
```

and you should see the default DVARS detection of outliers, giving something
like this (the exact output will depend on your own data):

```
data/group-00/sub-08/func/sub-08_task-taskzero_run-01_bold.nii.gz, [129 133 134]
data/group-00/sub-08/func/sub-08_task-taskzero_run-02_bold.nii.gz, [2]
data/group-00/sub-01/func/sub-01_task-taskzero_run-01_bold.nii.gz, []
...
ata/group-00/sub-03/func/sub-03_task-taskzero_run-01_bold.nii.gz, [  0  25  26  75  77  78  79  80 102 103 129 156 160]
data/group-00/sub-04/func/sub-04_task-taskzero_run-01_bold.nii.gz, []
data/group-00/sub-04/func/sub-04_task-taskzero_run-02_bold.nii.gz, [ 22  23  76  77 103 104]
```

## Your task

This is already an outlier detection method, but a very crude one, using a
fixed threshold of 2 x the interquartile range on the DVARS values to detect
outliers.

Your job, should you chose to accept it, is to improve the code so that the
`find_outliers.py` script does a better job at detecting outliers.

How do you know you have done a good job?  Well - that is the key question.

At a first pass, we would like you to *investigate* the FMRI time-series, by
looking at various measures of the scans, and looking at the scans themselves,
to see whether you can identify artifacts.

In due course, the thing we are going to evaluate, is how well you *recover the
activation pattern*, when you exclude these scans.  By *recover the activation
pattern*, we mean, how well does a statistical analysis do, using the task
regressors, in finding the activation pattern, after you exclude the outliers?
In particular, do you do a better job of recovering the activation pattern
after removing the outliers?   And can removing another set of outliers do a
better job?

But how will you tell whether you are doing a better job of recovering the
activation?

We will soon send you another PR, that gives you a basic script to do a
statistical analysis on an FMRI run, and generate an activation image, given
some identified outlier scans. This will use the machinery we will be teaching
over the next few weeks. But even this is not automated.  So, part of your job
here is to look at the activation images to see if you believe the result,
after your outlier estimation.

We will do something more sophisticated, and you may want to replicate this later.
We will use other datasets (that you don't have) from the same FMRI series, to
estimate the correct activation, and then compare your activation estimate,
after excluding outliers, to the estimate from other datasets.  If you've done
a good job, your estimate will be closer to the estimation from the other
datasets, on the assumption that the datasets do not share noise from their
outliers.  We will talk more about this in later sessions.  But, for now, your
job will be to look at how you are doing, by eye.

You should add a text file giving a brief summary for each outlier scan, why
you think the detected scans should be rejected as an outlier, and your
educated guess as to the cause of the difference between this scan and the rest
of the scans in the run.

## Grading

We will rate you on:

* The quality of your outlier detection as assessed by the improvement in the
  statistical testing for the experimental model after removing the outliers — as
  above.
* The generality of your outlier detection as assessed by the improvement in
  the statistical testing for the experimental model after removing the
  outliers, for another similar dataset.
* The quality of your code.  How easy is your code to read, and understand?  Is
  it well formatted, and well organized into different files and functions.
* The quality and transparency of your process, from your interactions on
  Github.
* The quality of your arguments about the scans rejected as outliers, in the
  text file above.

Your outlier detection script should be *reproducible*.

That means that we, your instructors, should be able to clone your repository,
and then follow simple instructions in order to be able to reproduce your run
of `scripts/find_outliers.py data` and get the same answer.

To make this possible, fill out the `README.md` text file in your repository to
describe a few simple steps that we can take to set up on our own machines and
run your code.  Have a look at the current `README.md` file for a skeleton.  We
should be able to perform these same steps to get the same output as you from
the outlier detection script.

## The sketch

The purpose of the `analysis_plan.md` document is for you to record your first
thoughts about how you will approach the problem.

* Do you need to arrange times to meet online or IRL to discuss progress, or
  can you collaborate by messaging back and forth via the Github interface, PRs
  and issues?
* What will you explore for your outlier detection?  For example, the current
  script only uses DVARS with a fixed threshold — will you use other metrics
  instead, or as well?  What metrics?   Will you want to adjust thresholds by
  hand?  Or work out automatic thresholds?  What would the interface to such
  code look like?
* Do you want to consider more advanced techniques such as [Principal Component
  Analysis](https://matthew-brett.github.io/teaching/pca_introduction.html) or
  even [Independent Component
  Analysis](https://en.wikipedia.org/wiki/Independent_component_analysis)?  We
  won't cover those techniques in this course, so if you use them, you should
  make sure you explain them in your write-up, and show us that you understand
  them to a reasonable level.
* Even for DVARS - how will you use the values?  For example, imagine someone
  moves instantaneously between scans 5 and 6.  There is a big DVARS value
  between 5 and 6 because of the movement signal in 6, so 6 may be an outlier —
  but what would you expect to see in scan 7?  If scan 7 is pretty similar to
  scan 6, it is also an outlier?
* You do not have to restrict yourself to just identifying outliers if you
  would prefer to go further.  For example, you could also propose regressors
  to go into your statistical estimation to allow for any artifacts that you
  have detected.  If so, you will need to create these regressors, and explain
  how they should be used, giving reproducible code for their use on your given
  dataset.
* We suggest you plan a literature review on outlier detection in functional
  MRI, and write this into your plan, and summarize in your project files in due
  course.

## That's it

Good luck.

Remember to ask for help early and often.

Now on to `analysis_plan.md`.
