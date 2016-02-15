A machine learning workspace based on ml pipelines.
the structure constructed by four parts: preprocess, feature generation, training, evaluation
1. preprocess part includes data clean, transfer, join, etc.  the output of this part is a formated raw features (often a csv included all things we want to do training)
2. feature generation part includes a series tranfer function to do feature engineering, for example: transfer one numerical value feature to multiple discrete binary (0, 1) value feature, join muliple features to generate another new feature, or to do in-place scale, etc.
3. training part design the training strategies, such as boosting, stack training, etc.
4. evaluation part design the predict and evaluate strategy.