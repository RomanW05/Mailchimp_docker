CREATE TABLE IF NOT EXISTS public.campaign_status
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    fk_subscriber_id integer,
    fk_campaign_id integer,
    section integer,
    "timestamp" time with time zone DEFAULT now(),
    fk_os_id integer,
    fk_browser_id integer,
    fk_country_id integer,
    fk_city_id integer,
    ip character varying(16) COLLATE pg_catalog."default",
    CONSTRAINT campaign_status_pkey PRIMARY KEY (id),
    CONSTRAINT fk_browser_id FOREIGN KEY (fk_browser_id)
        REFERENCES public.browsers (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_city_id FOREIGN KEY (fk_city_id)
        REFERENCES public.cities (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_country_id FOREIGN KEY (fk_country_id)
        REFERENCES public.countries (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_newsletter_campaign_id FOREIGN KEY (fk_campaign_id)
        REFERENCES public.campaign (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_os_id FOREIGN KEY (fk_os_id)
        REFERENCES public.os (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_subscribers_id FOREIGN KEY (fk_subscriber_id)
        REFERENCES public.subscribers (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.campaign_status
    OWNER to postgres;