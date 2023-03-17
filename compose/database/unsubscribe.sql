CREATE TABLE IF NOT EXISTS public.unsubscribe_info
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    fk_subscriber_id integer,
    fk_newsletter_id integer,
    fk_template_id integer,
    "timestamp" time with time zone DEFAULT now(),
    CONSTRAINT unsubscribe_info_pkey PRIMARY KEY (id),
    CONSTRAINT fk_newsletter_id FOREIGN KEY (fk_newsletter_id)
        REFERENCES public.campaign (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_subscriber_id FOREIGN KEY (fk_subscriber_id)
        REFERENCES public.subscribers (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_template_id FOREIGN KEY (fk_template_id)
        REFERENCES public.templates (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.unsubscribe_info
    OWNER to postgres;