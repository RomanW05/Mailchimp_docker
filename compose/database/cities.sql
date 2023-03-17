CREATE TABLE IF NOT EXISTS public.cities
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    fk_country_id integer,
    name character varying(128) COLLATE pg_catalog."default",
    CONSTRAINT cities_pkey PRIMARY KEY (id),
    CONSTRAINT fk_country_id FOREIGN KEY (fk_country_id)
        REFERENCES public.countries (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cities
    OWNER to postgres;