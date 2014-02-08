SciGen: Scilab Macro Builder
============================

I get bored with the legwork involved creating well-documented Scilab
macros/functions. The lack of integration of documentation and code
makes it all too easy to create lazily written (wrt documentation)
functions.

Most function design follows similar patterns, so I have been knocking
this up to automate some of it both for the sake of maintaining
libraries with very similar functions and make creating new macros
easier and more design friendly.

The generator/builder is written in Python. Why use Scilab? I have a
lot of legacy code in there and it also still serves a purpose for
scientific/data driven programming.

Design Overview
---------------

A Scilab macro (conventionally named `*.sci`) can be described in a
[DOM][]-like way.

![.sci "DOM"][doc/dom.jpg]

At least, this is what a well-written scilab macro should look like.

  - It may belong to a library.
  - It should have credits and licensing (which may be shared with
    other files in the library)
  - It contains at least one function (I'm not bothered about scripts
    here, conventionally named `*.sce`). They are generally bespoke
	and not so re-usable.

The functions themselves also have common features.

  - Function structural syntax
  - Help/Documentation comments
  - Parameter checking (!)
  - Function body

The Help/Documentation comment block should contain some or all of the
following:

  - Summary
  - Description
  - Parameter details / usage
  - Examples
  - Metadata
  - Credits / References

This macro generator (or writer... or builder) takes these constituent
parts defined ...elsewhere, encapsulates the data and then writes it
to a file as a scilab macro. Clearly if one wants to update, say, the
copyright or author a unix utility like `sed` does just fine but for a
library there may be changes to all files that are less simplistic.
Although maintaining is an intent of this (the idea of modifying the
content or logic of 20 similar-but-not-identical files in a library
makes me sad.

[DOM]: http://en.wikipedia.org/wiki/Document_Object_Model
