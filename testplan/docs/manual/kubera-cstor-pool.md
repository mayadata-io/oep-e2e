---
id: kubera-cstor-pool
title: Kubera Manual Testing Cstor Pool 
sidebar_label: Kubera cstor pool 
---

### Below test cases are executed manully for cstor pool


#### To verify the cspc creation from director 
- cspc should get created 

#### Delete CSPC created via director which has no volume 
- cspc should get deleted 

#### Delete CSPC not created via director which has no volume 
- cspc should get deleted 

#### Delete SPC which has no volume
- spc should get deleted 

#### Delete CSPC created via director which has volume
- Error message should be shown

#### Delete CSPC not created via director which has volume
- Error message should be shown

#### Delete SPC which has no volume
- Error message should be shown
