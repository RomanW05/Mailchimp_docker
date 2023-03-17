CREATE TABLE IF NOT EXISTS public.subscribers
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(64) COLLATE pg_catalog."default" NOT NULL,
    email character varying(128) COLLATE pg_catalog."default" NOT NULL,
    "timestamp" timestamp with time zone DEFAULT now(),
    CONSTRAINT subscribers_pkey PRIMARY KEY (id),
    CONSTRAINT email_unique UNIQUE (email)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.subscribers
    OWNER to postgres;

-- Trigger: insert_subscriber_status

-- DROP TRIGGER IF EXISTS insert_subscriber_status ON public.subscribers;

CREATE TRIGGER insert_subscriber_status
    AFTER INSERT
    ON public.subscribers
    FOR EACH ROW
    EXECUTE FUNCTION public.new_subscriber();