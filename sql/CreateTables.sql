CREATE TABLE jam_2015."MasterBatchCodes"
(
  
             "MCode" character(2) NOT NULL,
  
             "JamName" character varying(45),
  
       CONSTRAINT "MCode_Pri" PRIMARY KEY ("MCode")
)
       
WITH (
  OIDS=FALSE
);


ALTER TABLE jam_2015."MasterBatchCodes"
  OWNER TO postgres;


CREATE TABLE jam_2015."BatchList"
    
         (
  "MCode" character(2) NOT NULL,
  
                "BatchNumber" integer NOT NULL,
  
                "Jars_8oz" integer,
  
                "Jars_4oz" integer,
  
                "Jars_12oz" integer,
  
                "Batch_date" date,
  
                "Date_inserted" timestamp with time zone,
  
       CONSTRAINT "JamBatchs_pri" PRIMARY KEY ("MCode", "BatchNumber")
)
       
WITH (
  OIDS=FALSE
);


ALTER TABLE jam_2015."BatchList"
  OWNER TO postgres;

