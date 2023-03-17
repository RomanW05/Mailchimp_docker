CREATE TABLE IF NOT EXISTS public.subscriber_status
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    fk_subscriber_id integer,
    status boolean NOT NULL DEFAULT true,
    "timestamp" timestamp with time zone DEFAULT now(),
    CONSTRAINT subscriber_status_pkey PRIMARY KEY (id),
    CONSTRAINT fk_subscriber_id_unique UNIQUE (fk_subscriber_id),
    CONSTRAINT id UNIQUE (id)
        INCLUDE(id),
    CONSTRAINT fk_subscriber_id FOREIGN KEY (fk_subscriber_id)
        REFERENCES public.subscribers (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.subscriber_status
    OWNER to postgres;