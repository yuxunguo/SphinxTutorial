..  if you put .. without any things else, it's consider comments
    More lines can be added as long as they are in the same block

Introduction
=============

Subsection
----------

Subsubsection
~~~~~~~~~~~~~~

Section/subsection/subsection title can be added by addressing them with '===='/'------'/'~~~~~~'

Paragraph and List
-------------------
New paragraph can be created with a empty line inbetween.

This is a new paragraph.

| If you don't want a completely new paragraph. 
| '|' Creates force-line-break paragraph with empty lines before and after

| This is an example
| of paragraph
| that force the line-break.

'-' and '*' start list with dot, '#.' start numbered list, with empty lines before and after the lists.

- This is 
  
    - You can 
    - do sublist
    - but still need empty lines before and after the sublist
  
- an example of dotted lists with '-' or '*'
- | You can also do force line-break for each item
  | if you find certain item need this.

#. This is

    - You can 
    - do mixed-type sublist
    - but still need empty lines before and after the sublist
  
#. an
#. example of numbered lists with '#.' 

Commands and enviroment
-----------------------
Two types of command are allowed: inline or stand-out

| First, inline code block can be addressed by `` something`` e.g. ``code``.
| Note that there should be no space after `` or ` , otherwise it will be recongized as a symbol.
| Second, hyperlink can be added with  ` Name <link>`_, e.g. `Sphinx-Tutorial Git Page <https://github.com/yuxunguo/SphinxTutorial>`_ (noting the last underline after the ` )

Other inline commands can be used as ``:inlinecommand:`input``` similar to the ``\inlinecommand{input}``  syntax in LaTeX. For instance,

- ``:ref:`something``` generates a link to some module, e.g., :ref:`module1 module`, 
- ``:math:`something``` generates a math expression with LaTeX syntax, e.g., :math:`\xi+\pi`
- ``:func:`something``` generates a link to function, e.g. :func:`module1.Module1_TestFunc1`
- | ``:meth:`something``` generates a link to a meth in class, e.g. :meth:`module1.Module1_TestFunc1`
  | (it seems ``:func:`` and ``:meth:`` are practically the same but the copilots distinguish them.)

The reference name of functions/method are their names by default, and the reference name for the module are their section names. But they can be customized.

The stand-out enviroment can be create with command ``.. command :: options`` with empty lines before and after, as well as a following section as the input, similar to the ``\begin{command} \end{command}`` syntax of LaTeX.

For instance,

- ``.. code-block:: py`` generates a python code block
  
  .. code-block:: py

     import pandas as pd
     import os
     dir_path = os.path.dirname(os.path.realpath(__file__))
- ``.. math::`` generates a stand-out math expression with LaTeX syntax

  .. math::

      f(a)=\sum_{i=1}^{\infty}\frac{i^4}{\pi} a_i


The commands of reStructuredText can be used in the docstring documentations and follows the same rules!