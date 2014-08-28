# CFEngine Beautifier

CFEngine configuration file beautifier written in Python. It can be used standalone or via Sublime Text.

- Integrates with Sublime Text 2 and Sublime Text 3.
- Installation for Sublime by cloning into Sublime Text's Packages folder. Installation via Package Manager coming soon.

#### Sublime Text Options

<table>
  <tr>
    <td>Option</td>
    <td>Description</td>
    <td>Value</td>
    <td>Default</td>
  </tr>
  <tr>
    <td>beautify_on_save</td>
    <td>Run beautifier every time the file is saved</td>
    <td>true | false</td>
    <td>true</td>
  </tr>
  <tr>
    <td>page_width</td>
    <td>Tries to make text fit onto this width (number of characters)</td>
    <td>number</td>
    <td>100</td>
  </tr>
  <tr>
    <td>remove_empty_promise_types</td>
    <td>Remove promise types (such as vars:, reports:) which have no promises or comments</td>
    <td>true | false</td>
    <td>true</td>
  </tr>
  <tr>
    <td>sort_promise_types_to_evaluation_order</td>
    <td>Sort promise types to CFEngine normal order</td>
    <td>true | false</td>
    <td>true</td>
  </tr>
</table>

#### Command Line Options

Run cf-beautify --help

#### Installation

##### Manual Install with ST3
cd ~/.config/sublime-text-3/Packages
git clone https://github.com/naksu/cfengine_beautifier.git CFEngineBeautifier

