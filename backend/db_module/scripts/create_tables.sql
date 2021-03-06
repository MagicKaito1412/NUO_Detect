-- Table: public.users

CREATE TABLE IF NOT EXISTS public.users
(
    user_id      bigserial                                          NOT NULL,
    password     character varying(60) COLLATE pg_catalog."default" NOT NULL,
    login        character varying(30) COLLATE pg_catalog."default" NOT NULL,
    access_level integer                                            NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (user_id),
    CONSTRAINT users_login_key UNIQUE (login)
)
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to u1;

INSERT INTO public.users (user_id, login, password, access_level)
VALUES (nextval(pg_get_serial_sequence('users', 'user_id')), 'admin', 'admin0000', 1);

-- Table: public.patients

CREATE TABLE IF NOT EXISTS public.patients
(
    patient_id  bigserial                                          NOT NULL,
    user_id     bigint                                             NOT NULL,
    first_name  character varying(30) COLLATE pg_catalog."default" NOT NULL,
    last_name   character varying(50) COLLATE pg_catalog."default" NOT NULL,
    middle_name character varying(50) COLLATE pg_catalog."default",
    gender      integer                                            NOT NULL,
    birth_date  timestamp without time zone,
    age         integer,
    weight      integer                                            NOT NULL,
    height      integer                                            NOT NULL,
    policy_num  character varying(19) COLLATE pg_catalog."default" NOT NULL,
    email       character varying(50) COLLATE pg_catalog."default",
    has_nuo     integer,
    telephone   character varying(19),
    has_probs   boolean,
    bmi         real                                               NOT NULL,
    CONSTRAINT patients_pkey PRIMARY KEY (patient_id),
    CONSTRAINT patients_user_id_key UNIQUE (user_id),
    CONSTRAINT patients_policy_num_key UNIQUE (policy_num),
    CONSTRAINT patients_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.users (user_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;

ALTER TABLE public.patients
    OWNER to u1;

-- Table: public.doctors

CREATE TABLE IF NOT EXISTS public.doctors
(
    doctor_id   bigserial                                          NOT NULL,
    user_id     bigint                                             NOT NULL,
    first_name  character varying(30) COLLATE pg_catalog."default" NOT NULL,
    last_name   character varying(50) COLLATE pg_catalog."default" NOT NULL,
    middle_name character varying(50) COLLATE pg_catalog."default",
    cabinet     real,
    telephone   character varying(19)                              NOT NULL,
    email       character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT doctors_pkey PRIMARY KEY (doctor_id),
    CONSTRAINT doctors_user_id_key UNIQUE (user_id),
    CONSTRAINT doctors_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.users (user_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;

ALTER TABLE public.doctors
    OWNER to u1;


-- Table: public.ekgs

CREATE TABLE IF NOT EXISTS public.ekgs
(
    ekg_id          bigserial                   NOT NULL,
    patient_id      bigint                      NOT NULL,
    registry_date   timestamp without time zone NOT NULL,
    sdnn            float,
    skewness        float,
    amo             float,
    swai            float,
    mo              float,
    drr             float,
    rrnn            float,
    pnn50           float,
    si              float,
    sati            float,
    rmi             float,
    kurtosis        float,
    cv              float,
    rmssd           float,
    nn50            float,
    lf              float,
    lfhf            float,
    hfp             float,
    ulf             float,
    tp              float,
    vlf             float,
    vlfp            float,
    lfp             float,
    br              float,
    ulfp            float,
    ic              float,
    hf              float,
    tpfull          float,
    p_left_slopes   float,
    p_right_slopes  float,
    q_left_slopes   float,
    q_right_slopes  float,
    t_left_slopes   float,
    t_right_slopes  float,
    qt              float,
    st              float,
    p               float,
    pq              float,
    qrs             float,
    pulse           integer,
    prob_log_reg    real,
    prob_rnd_forest real,
    prob_log_svm    real,
    has_nuo         integer,
    CONSTRAINT ekgs_pkey PRIMARY KEY (ekg_id),
    CONSTRAINT ekgs_patient_id_fkey FOREIGN KEY (patient_id)
        REFERENCES public.patients (patient_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;

ALTER TABLE public.doctors
    OWNER to u1;