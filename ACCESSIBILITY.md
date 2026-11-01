# Accessibility

TorchFoundry aims to make machine learning development more approachable and accessible to everyone. Accessibility is an important part of building software that people with different abilities, experience levels, and working environments can understand, use, and contribute to.

As a Python library, TorchFoundry does not currently provide a graphical user interface. Its accessibility efforts therefore focus primarily on clear documentation, readable code examples, understandable error messages, and an inclusive development and contribution process.

This document describes our accessibility priorities, expectations for contributors, known limitations, and how to report accessibility barriers.

## Priorities

TorchFoundry prioritizes the following areas:

* **Clear documentation:** Documentation should use understandable language, consistent terminology, and a logical structure.
* **Readable examples:** Code examples should be properly formatted, explained where necessary, and easy to follow.
* **Understandable errors:** Error messages should provide useful information that helps users identify and resolve problems.
* **Inclusive contributions:** Contributors should be able to participate without unnecessary barriers, regardless of their experience level or abilities.
* **Accessible project resources:** Repository documentation, issue templates, and contribution instructions should be structured and readable.
* **Compatibility:** TorchFoundry should avoid introducing unnecessary restrictions that make it harder to use common development tools and workflows.

We recognize the Web Content Accessibility Guidelines (WCAG) as a useful reference for accessible web content. However, TorchFoundry does not currently claim conformance with any WCAG level. Any future conformance claims will be made only after an appropriate evaluation.

## Contributor expectations

We encourage all contributors to consider accessibility when introducing or modifying features, documentation, and examples.

Contributors should:

* Write documentation using clear and straightforward language.
* Use descriptive names for public functions, classes, parameters, and variables.
* Include meaningful error messages when handling invalid input or unsupported operations.
* Keep code examples readable and provide explanations when the intended behavior is not obvious.
* Use descriptive headings and maintain a logical structure in Markdown documentation.
* Avoid relying exclusively on color, visual formatting, or symbols to communicate important information.
* Consider users who rely on keyboard navigation, screen readers, or other assistive technologies when modifying any user-facing project resources.
* Report known accessibility barriers introduced by a contribution.

For changes affecting documentation or other user-facing resources, contributors should review the result for readability, structure, and usability.

Accessibility improvements are welcome even when they do not introduce new functionality.

## Reporting accessibility issues

If you encounter an accessibility barrier while using TorchFoundry, reading its documentation, or contributing to the project, please report it through the repository's GitHub Issues.

When reporting an issue, useful information includes:

* A description of the task you were trying to complete.
* The part of TorchFoundry or its documentation where the problem occurred.
* What you expected to happen and what actually happened.
* Your operating system and relevant software versions.
* Your browser, if the issue involves web-based documentation or GitHub.
* Any assistive technology involved, if relevant.

Screenshots, recordings, and code examples are welcome but entirely optional.

You do not need to disclose a disability or provide personal medical information to report an accessibility issue.

Please use a private reporting method if your report contains sensitive security information. Accessibility reports themselves should generally be submitted as regular GitHub Issues.

### Severity

Accessibility issues may be classified according to how significantly they prevent someone from using or contributing to TorchFoundry.

The following levels provide guidance:

| Severity | Description                                                                                                                  | Example                                                                                                   |
| -------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Critical | A major barrier prevents users from accessing essential project functionality or information, with no reasonable workaround. | Essential documentation is completely inaccessible to a user relying on assistive technology.             |
| High     | A significant barrier makes an important task extremely difficult or prevents its completion for some users.                 | A key installation or usage instruction cannot be accessed or understood through an assistive technology. |
| Medium   | A barrier makes certain tasks more difficult, but a reasonable workaround exists.                                            | Poorly structured documentation makes navigating a long guide difficult.                                  |
| Low      | A minor usability or accessibility improvement that does not significantly prevent task completion.                          | Inconsistent heading structure or unclear descriptions in an example.                                     |

Maintainers may assign or adjust severity during issue triage. Reporters do not need to determine the severity themselves.

### How we respond

We aim to handle accessibility reports respectfully and transparently.

When an accessibility issue is reported, maintainers will aim to:

1. Review the report and understand the affected experience.
2. Confirm the issue and determine its impact.
3. Assign an appropriate priority.
4. Discuss possible improvements or workarounds.
5. Provide updates when meaningful progress is made.
6. Where possible, ask the reporter to verify that the proposed fix addresses the original barrier.

TorchFoundry is maintained on a best-effort basis. We cannot guarantee fixed response or resolution times, but accessibility reports will be considered as part of normal project maintenance and prioritization.

## Ownership and maintenance

Accessibility is the responsibility of the TorchFoundry maintainers and contributors.

The project maintainer is responsible for:

* Reviewing reported accessibility issues.
* Considering accessibility when reviewing contributions.
* Maintaining this document as the project evolves.
* Prioritizing accessibility improvements where practical.

This document should be reviewed periodically and whenever significant changes affect the project's user-facing resources or contribution process.

If project maintenance responsibilities change, accessibility ownership should transfer to the new maintainers.

## Supported environments

TorchFoundry is a Python library and primarily operates within the Python development environment.

Its functionality depends on the installed Python version, PyTorch, and other project dependencies.

The project does not currently maintain a formally tested accessibility compatibility matrix for assistive technologies, browsers, or operating systems.

For the project's supported Python versions and dependencies, refer to the installation instructions and project configuration.

Accessibility of the documentation and repository may also depend on the platform used to access them.

We welcome reports about compatibility problems involving assistive technologies, development environments, and operating systems.

## Known limitations

TorchFoundry currently has no dedicated graphical user interface. Most interactions take place through Python code, terminal output, documentation, and development tools.

This means that some accessibility considerations, such as visual interface navigation and screen-reader interaction with application controls, do not directly apply to the library itself.

However, this does not mean that the project is free of accessibility barriers.

Potential limitations may include:

* Documentation that could be easier to navigate or understand.
* Code examples that may require additional explanations.
* Terminal output or error messages that could be clearer.
* Accessibility limitations inherited from external tools, dependencies, or hosting platforms.

Known issues should be reported and tracked through GitHub Issues. This section will be updated as limitations are identified and improvements are made.

## Feedback and improvements

Accessibility is an ongoing process, not a one-time feature.

We welcome suggestions, reports, and contributions that make TorchFoundry easier to understand, use, and contribute to.

Whether you identify a significant accessibility barrier or a small improvement to documentation, your feedback is valuable to the continued development of the project.

Thank you for helping make TorchFoundry more accessible.

