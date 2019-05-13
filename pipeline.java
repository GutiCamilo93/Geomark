
pipeline.apply(PubsubIO.Read.timestampLabel("created_at").topic("projects/servinf-geomark-social-prod/topics/sentiment"))
	.apply(ParDo.of(new DoFn<String, TableRow>(){
	      @Override
	      public void processElement(ProcessContext c) {

	    	TableRow row = new TableRow();
	    	try{
	    		JSONParser parser = new JSONParser();
	    		
	    		Object obj = parser.parse(c.element());
	    		JSONObject jsonObject = (JSONObject) obj;
	    		String text = (String) jsonObject.get("text");
	    		
	    		Analyze analyze = new Analyze(Analyze.getLanguageService());
	    		Sentiment sentiment = analyze.analyzeSentiment(text);
	    		
	    		List<Token> tokens = analyze.analyzeSyntax(text);
	    		JSONArray jsonTokens = new JSONArray();
	    		for (Token token : tokens){
	    			JSONObject jsonToken = new JSONObject();
	    			jsonToken.put("partOfSpeech", token.getPartOfSpeech().getTag());
	    			jsonToken.put("content", token.getText().getContent());
	    			jsonTokens.add(jsonToken);
	    		}
	    		row.set("tweet_object", c.element())
	    		.set("syntax", jsonTokens.toJSONString())
	    		.set("polarity", sentiment.getPolarity())
	    		.set("magnitude", sentiment.getMagnitude());
	    	}
	      	catch (ParseException | IOException | GeneralSecurityException e) {
	      		row.set("tweet_object", e.toString());
	      	}
	    	c.output(row);
	      }
	}))
	.apply(BigQueryIO.Write.to(getTableReference()).withCreateDisposition(CreateDisposition.CREATE_IF_NEEDED).
			withWriteDisposition(WriteDisposition.WRITE_APPEND).withSchema(getSchema()));
	pipeline.run();
