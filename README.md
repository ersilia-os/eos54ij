# Cardiac Toxicity Prediction

Pred-hERG is a deep neural network trained on a ChEMBL based dataset of hERG experimentally validated blockers/non-blockers. The code and training data are not released, using this model posts predictions to the LabMol online server.

## Identifiers

* EOS model ID: `eos54ij`
* Slug: `pred-herg`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability that the molecule is a hERG non-blocker or a blocker / Multiclass models return three probabilities (non-blocker, weak blocker and strong blocker). Finally, a probability map with atoms in green that contribute towards hERG blockade and atoms in red thatdecrease hERG blockade (threshold for classification: 10 uM)

## References

* [Publication](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5720373/pdf/nihms854187.pdf)
* [Source Code](http://predherg.labmol.com.br/)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos54ij)

## Citation

If you use this model, please cite the [original authors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5720373/pdf/nihms854187.pdf) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!