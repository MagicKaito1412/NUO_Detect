-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    user_id      bigint                                             NOT NULL,
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

-- Table: public.patients

-- DROP TABLE public.patients;

CREATE TABLE IF NOT EXISTS public.patients
(
    patient_id      bigint                                             NOT NULL,
    user_id         bigint                                             NOT NULL,
    first_name      character varying(30) COLLATE pg_catalog."default" NOT NULL,
    last_name       character varying(50) COLLATE pg_catalog."default" NOT NULL,
    middle_name     character varying(50) COLLATE pg_catalog."default",
    gender          integer                                            NOT NULL,
    age             integer                                            NOT NULL,
    weight          integer                                            NOT NULL,
    height          integer                                            NOT NULL,
    has_nuo         boolean,
    prob_log_reg    real,
    prob_rnd_forest real,
    prob_log_svm    real,
    CONSTRAINT patients_pkey PRIMARY KEY (patient_id),
    CONSTRAINT patients_user_id_key UNIQUE (user_id),
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

-- DROP TABLE public.doctors;

CREATE TABLE IF NOT EXISTS public.doctors
(
    doctor_id bigint                                              NOT NULL,
    user_id   bigint                                              NOT NULL,
    full_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    cabinet   real,
    telephone integer                                             NOT NULL,
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

-- DROP TABLE public.ekgs;

CREATE TABLE IF NOT EXISTS public.ekgs
(
    ekg_id         bigint NOT NULL,
    patient_id     bigint NOT NULL,
    registry_date  date   NOT NULL,
    sdnn           float,
    skewness       float,
    amo            float,
    swai           float,
    mo             float,
    drr            float,
    rrnn           float,
    pnn50          float,
    si             float,
    sati           float,
    rmi            float,
    kurtosis       float,
    cv             float,
    rmssd          float,
    nn50           float,
    lf             float,
    lfhf           float,
    hfp            float,
    ulf            float,
    tp             float,
    vlf            float,
    vlfp           float,
    lfp            float,
    br             float,
    ulfp           float,
    ic             float,
    hf             float,
    tpfull         float,
    p_left_slopes  float,
    p_right_slopes float,
    q_left_slopes  float,
    q_right_slopes float,
    t_left_slopes  float,
    t_right_slopes float,
    qt             float,
    st             float,
    p              float,
    pq             float,
    qrs            float,
    pulse          integer,
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