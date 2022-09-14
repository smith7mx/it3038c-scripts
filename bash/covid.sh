#!/bin/bash

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
DEATH=$(echo $DATA | jq '.[0].death')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
PENDING=$(echo $DATA | jq '.[0].pending')
echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative cases, $DEATH deaths, and $PENDING pending cases."

