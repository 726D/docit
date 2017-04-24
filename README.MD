# Trace changed features in bdd tests for the documentation

## Current state
docit is currently not production ready by far. Sorry for that. At the moment it just serves as proof of concept for one approach for one aspect of the bigger problem.

## Prerequisites for testing

* checkout https://github.com/gabrielfalcao/lettuce
* checkout docit

## Testing

0. change to the directory containg the project you want to generate the report for
1. git difftool -y --extcmd /{PathTo}/docit/docitdiff.py 0.2.5 0.2.7  >> out.html
2. have a look at out.html
3. remove out.html in a browser
4. GOTO 1 and try other tags :)

## What for this crap

The current code just sketches one possible approach for one part of the problem.

* it focusses just on the .feature files of bdd tests and isn't flexible/configurable. 
* the output is not really nice 
* the workflow is hacky

But the person in charge of keeping the end user documentation in sync gets a report about
* new .features files -> probably a new feature to include in the documentation
* deletetd .features files -> probably a feature to remove from  the documentation
* changed .features files -> most likely a feature that has to be changed in the documentation
 
One shortcoming right now is, that remote files currently ars shown as tmp files. That can be fixed with more work (e.g. as sketched in notes.txt. first get list of files with correct filename and  modification status, then iterate over the list)
Unchanged features are not reported as that would be a waste of time. If wanted that can be changed with more work.

The core idea of this aproach used  is to (mis)use the difftool: git difftool -y --extcmd /path/to/customDiffToolThatCreatesTheReport not for diffing but for reporting. That way you get both files delivered by git and could work with their content without having to take care of checking them out, writing them to a tmp space and without to have to clean up afterward.
Having both files local allows to 
* use thm for the report 8done)
* do more filtering, searching for custom tags (usecase, ..) that allow matching documentation and test more closely. 

### Background
The loop over issue tickets, code changes, tests, test results normally in sync. The documentation often is not in sync with this loop. There should be methods and tools to change that.
Some aspects oft this problems are:
* inform the person in charge of keeping the end user documentation in sync about changes -> here via changes in the bdd .features 
* give him information about the changes -> here via html report
* enhance cohesion between bdd features, documentation fragments and the final documentations -> here custom tags would com into play + some automated workflow (generate updated docbook, wiki updates, ... )

### Solved problem
* Easily find and compare changed files and generate a report/diff for them. 
* "Innovative" way to use git for the tedious work.

### Future work
Think about a usable workflow and start to implement that from scratch.




 




