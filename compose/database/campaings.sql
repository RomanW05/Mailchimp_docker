CREATE TABLE IF NOT EXISTS public.campaign
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(128) COLLATE pg_catalog."default",
    "timestamp" time with time zone DEFAULT now(),
    CONSTRAINT campaign_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.campaign
    OWNER to postgres;