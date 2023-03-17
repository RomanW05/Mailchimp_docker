CREATE TABLE IF NOT EXISTS public.templates
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    "timestamp" timestamp with time zone DEFAULT now(),
    name character varying(50) COLLATE pg_catalog."default",
    plain_data character varying(1000000) COLLATE pg_catalog."default",
    html_data character varying(1000000) COLLATE pg_catalog."default",
    design_data character varying(1000000) COLLATE pg_catalog."default",
    CONSTRAINT templates_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.templates
    OWNER to postgres;