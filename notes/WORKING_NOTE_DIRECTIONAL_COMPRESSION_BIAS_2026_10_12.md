# Working note — Directional compression of consequential distinctions and bias

**Date:** 2026-10-12  
**Status:** WORKING HYPOTHESIS / proposed test design; no validated measurement or causal finding  
**Program connections:** Question-specific adequacy, human-facing mediation (Program E), question quality, recovery to primary sources

## Generating question

> **Did the distinctions lost through compression systematically favor a particular conclusion?**

Compression is unavoidable. A representation can contain individually true statements yet still produce a misleading overall impression by selectively retaining, suppressing, ordering, generalizing, or weighting distinctions. The research question is whether that selective loss can be measured **directionally**—with reference to the question the representation must answer—rather than treated as a vague allegation of bias.

A complementary hypothesis proposes that **independently established interests or preferred outcomes** may help predict which consequential distinctions an actor compresses out. That is a stronger, separate causal proposition. The observable pattern in an output must be established before inferring its source or motive.

## Provisional definition

**Directional compression bias**: a recurring, insufficiently justified asymmetry in the preservation, omission, prominence, or weighting of consequential distinctions that systematically shifts a representation toward a specified conclusion, relative to an evidence- and question-matched baseline.

This is one *candidate mechanism* of bias, not a complete definition of every kind of cognitive, statistical or institutional bias.

- **Distinction of consequence:** a source-grounded distinction whose presence, absence or misweighting could materially alter the answer, decision, calibrated uncertainty or follow-up demanded by a fixed question.
- **Direction:** the conclusion or decision toward which the representational change tends to move a reader.
- **Asymmetry:** differences in treatment that are not already justified by evidence quality, relevance, uncertainty, audience, or a legitimate space limit.
- **Systematic:** a repeated, prespecified pattern or controlled reversal. One striking example can generate a hypothesis, but cannot by itself demonstrate systematic bias.
- **Compression:** includes salience, sequence, omission, qualification and scope; facts need not be literally deleted to be functionally discounted.

**Candidate summary:** Bias may leave a detectable signature in the *directional loss or reweighting of consequential distinctions*.

### Claim levels that must remain separate

1. **Observable framing difference:** two accounts of the same evidence highlight different aspects.
2. **Consequential representational distortion:** those choices change what a recipient can correctly infer or decide under the *same* question.
3. **Systematic directional bias:** the distortion repeatedly favors a direction beyond what the available evidence and task warrant.
4. **Interest-aligned bias:** that direction corresponds to independently evidenced interests or incentives.
5. **Deliberate manipulation:** intention to steer or deceive; this requires independent evidence and does not follow from the output alone.

An output can be biased without proving the author's intent. An actor's interests can be known without proving a particular output is biased.

## Illustrative case: bacterium, mouse tumors, and opposed headlines

The motivating comparison involved a dramatic social-media description and a caution-oriented AI description of one 2025 *Gut Microbes* paper about a frog-derived strain of *Ewingella americana*:

- Primary paper: Iwata et al., [*Discovery and characterization of antitumor gut microbiota from amphibians and reptiles*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12710904/); [DOI 10.1080/19490976.2025.2599562](https://doi.org/10.1080/19490976.2025.2599562).
- The paper reports complete responses in a five-mouse *Colon-26* comparison treatment group after one intravenous dose. This is a striking **animal-model result**, not an established treatment for people. The model, sample size, dose constraints, and generalization limits matter.

| Compression direction | Legitimate emphasis | Distinctions at risk of underweighting |
| --- | --- | --- |
| Breakthrough-oriented | Strong tumor response and a promising therapeutic mechanism | Limited model and sample, safety, uncertainty of human translation |
| Debunking/caution-oriented | Safety, clinical uncertainty, mouse-to-human limits | Magnitude of the actual model-specific observation and why the mechanism may deserve investigation |

Neither direction is automatically bias. The public promotional headline **did specify mice**, and the cautionary account **did acknowledge tumor elimination in mice**. The consequential difference may lie in *scope and proportional emphasis*, rather than outright omission. A categorical opening judgment may steer interpretation despite later qualifying details; that is a testable possibility, not a proven effect.

The questions **“What did this mouse experiment find?”** and **“Does this establish a safe human cancer treatment?”** have legitimately different consequential distinctions. A cautious summary may be precisely adequate for the second question and insufficient for the first. The question must be fixed before calling a difference bias.

**Status of this case:** illustrative framing observation, not a completed content analysis or independent clinical appraisal. This example alone establishes neither systematic bias nor the interests or motives of any author, communicator, or AI system.

## How it fits Representation Science

Use the program's standard variables:

- **Reality / source:** the experimental system and its published evidence, with uncertainty.
- **Question `Q`:** the exact informational or decision obligation.
- **Representation `R`:** a summary or interpretive account.
- **Retained information:** facts, qualifiers, uncertainty and relationships accessible to the recipient.
- **Omitted / attenuated information:** consequential differences absent, softened or inaccurately amplified.
- **Recovery path:** whether the reader can re-enter the primary evidence, and at what cost.
- **Adequacy test:** whether `R` supports the correct bounded answer or appropriately calibrated uncertainty for `Q`.
- **Failure witness:** two source situations or two representations that a compressed view treats as equivalent despite requiring materially different conclusions for `Q`.

The new candidate variable is **the signed direction of consequential information loss**. Simple omission counts do not measure it. Legitimate evidence is often asymmetric; equally long pro and con lists can be *less* faithful than an unequal account.

A causal hypothesis worth testing later is:

`interests / incentives → selection and salience → compressed account → recipient judgment`

The last two links may be tested from texts and recipient outcomes. Establishing the first link, and especially intent, needs evidence *outside* the account.

## Proposed bounded experiment (not frozen, authorized, or run)

**Research question:** Can a repeatable measure detect directional loss/reweighting of consequential distinctions, under matched evidence, question, audience and compression budget, without merely detecting differences in writing style or legitimate evidence weighting?

**Freeze in advance:**

1. A versioned, self-contained evidence packet; the question and decision; the intended recipient; and equal length/token constraints.
2. An inventory of consequential distinctions developed blind to the representations and alleged interests, with relevance, reliability and uncertainty annotations.
3. Directional hypotheses, a neutral/null condition, negative controls, a reversal control, sample size and stop criteria.
4. The annotation rubric and reader-outcome scoring plan.

**Possible conditions:** neutral source-grounded reference summary; unconstrained summaries under the same instruction; explicitly promotional and explicitly cautionary positive controls; and counterfactual packets in which the identity or incentive labels are swapped without changing the facts.

**Measure separately:**

- whether each prespecified distinction is retained, omitted, misstated, amplified or attenuated;
- its placement, qualification and certainty;
- whether its detail is reconstructible from the representation or recoverable only by revisiting sources;
- inter-rater agreement under blind coding;
- recipient answers, confidence calibration, and decisions when only the summary is available;
- length, annotation cost and source-recovery cost.

**Evidence favoring the hypothesis:** a reliable, repeated asymmetry affecting *comparably consequential* distinctions, in a predeclared direction, surviving question and evidence-quality controls, with a measurable effect on recipient inference and (in controlled tasks) reversal when the directional pressure is reversed.

**Evidence against / failure conditions:** the asymmetry disappears after question alignment, has an evidence-quality justification, is not reproducible, does not alter decisions, depends on unblinded coding, or flags a source-faithful asymmetric summary as biased simply because evidence itself is asymmetric.

Do not invent a scalar “bias index” until the annotations are reliable and the metric has discriminative validity. It may be more informative to retain a vector of omission, attenuation, amplification, prominence and recovery costs.

## Safeguards against the detector's own bias

- **Fix the question first.** “Consequential” depends on what the representation must enable. An analyst can otherwise hand-pick losses that favor the analyst's theory.
- **Blind the evidence inventory.** Do not identify “important distinctions” by starting with the communicator's presumed interests.
- **Compare equally strong evidence.** Fair summary does not mean equal emphasis for unequally credible facts.
- **Seek nulls and reversals.** Test contexts in which the expected direction should vanish or flip.
- **Do not infer minds from texts.** Output bias, interest alignment, causal incentives and deliberate deception are distinct claims.
- **Track recoverability.** Missing surface detail does not always mean irrecoverable information, although a link that no reader follows may fail a human-facing decision task.
- **Keep the case source-public.** Do not publish private discussions, personal messages or sensitive records to demonstrate the phenomenon.

## Candidate program extension

Existing loop: **represent → compress → test → expose a lost distinction → enrich or replace → retest**.

Proposed additional audit: **declare the question → identify consequential distinctions independently → inspect the *direction* of loss and weighting → test the reader's inference → recover primary evidence → retest**.

This creates a sharper question for Program E:

> A representation may be compact and contain no literally false sentence, yet still steer a decision. What distinctions must remain visible or recoverable for the reader to resist that steering?

## Status and next step

**HYPOTHESIS / OPEN.** No experiment has been run; no general detector, intentionality inference or novelty claim is earned.

A useful next step is to construct a fully synthetic, source-complete example in which two equally short, individually truthful summaries induce different decisions. Predeclare the consequential distinctions before showing either summary, and include a second adversarial example designed to cause false bias detection. Only promote this into a formal experiment or Representation Record if the controlled results discriminate the hypothesis from ordinary, legitimate compression.
