SciGen: Scilab Macro Builder
============================

I get bored with the legwork involved creating well-documented Scilab
macros/functions. The lack of integration of documentation and code
makes it all too easy to create lazily written (wrt documentation)
functions.

Most function design follows similar patterns, so I have been knocking
this up to automate some of it both for the sake of maintaining
libraries with very similar functions and make creating new macros
easier.

The generator/builder is written in Python. Why use Scilab? I have a
lot of legacy code in there and it also still serves a purpose for
scientific/data driven programming.
