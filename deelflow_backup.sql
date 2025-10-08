--
-- PostgreSQL database dump
--

\restrict IccbhRcVDUGdGKGQWH39DDOtbr5ePNAMuS4bZ3tIkm0a0ODMkZg350kcFE2WLEp

-- Dumped from database version 16.10 (Ubuntu 16.10-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.10 (Ubuntu 16.10-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id bigint NOT NULL,
    name text
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id bigint,
    permission_id bigint
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id bigint NOT NULL,
    content_type_id bigint,
    codename text,
    name text
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id bigint NOT NULL,
    password text,
    last_login timestamp with time zone,
    is_superuser boolean,
    username text,
    last_name text,
    email text,
    is_staff boolean,
    is_active boolean,
    date_joined timestamp with time zone,
    first_name text
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id bigint,
    group_id bigint
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id bigint,
    permission_id bigint
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: deelflow_activityfeed; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_activityfeed (
    id bigint NOT NULL,
    user_id bigint,
    action_type text,
    description text,
    "timestamp" timestamp with time zone
);


ALTER TABLE public.deelflow_activityfeed OWNER TO postgres;

--
-- Name: deelflow_activityfeed_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_activityfeed_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_activityfeed_id_seq OWNER TO postgres;

--
-- Name: deelflow_activityfeed_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_activityfeed_id_seq OWNED BY public.deelflow_activityfeed.id;


--
-- Name: deelflow_blockchaintxnmetrics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_blockchaintxnmetrics (
    id bigint NOT NULL,
    total_txns bigint,
    success_rate real,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_blockchaintxnmetrics OWNER TO postgres;

--
-- Name: deelflow_blockchaintxnmetrics_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_blockchaintxnmetrics_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_blockchaintxnmetrics_id_seq OWNER TO postgres;

--
-- Name: deelflow_blockchaintxnmetrics_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_blockchaintxnmetrics_id_seq OWNED BY public.deelflow_blockchaintxnmetrics.id;


--
-- Name: deelflow_businessmetrics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_businessmetrics (
    id bigint NOT NULL,
    total_revenue numeric,
    active_users bigint,
    properties_listed bigint,
    total_deals bigint,
    monthly_profit numeric,
    voice_calls_count bigint,
    report_date date,
    ai_conversations numeric
);


ALTER TABLE public.deelflow_businessmetrics OWNER TO postgres;

--
-- Name: deelflow_businessmetrics_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_businessmetrics_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_businessmetrics_id_seq OWNER TO postgres;

--
-- Name: deelflow_businessmetrics_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_businessmetrics_id_seq OWNED BY public.deelflow_businessmetrics.id;


--
-- Name: deelflow_campaign; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_campaign (
    id bigint NOT NULL,
    name text,
    status text,
    created_at timestamp with time zone,
    budget numeric,
    campaign_type text,
    channel text,
    distress_indicators text,
    email_content text,
    geographic_scope_type text,
    geographic_scope_values text,
    location text,
    max_price numeric,
    min_price numeric,
    minimum_equity numeric,
    property_type text,
    scheduled_at timestamp with time zone,
    subject_line text,
    use_ai_personalization boolean
);


ALTER TABLE public.deelflow_campaign OWNER TO postgres;

--
-- Name: deelflow_campaign_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_campaign_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_campaign_id_seq OWNER TO postgres;

--
-- Name: deelflow_campaign_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_campaign_id_seq OWNED BY public.deelflow_campaign.id;


--
-- Name: deelflow_campaignperformance; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_campaignperformance (
    id bigint NOT NULL,
    campaign_type text,
    roi_percentage numeric,
    date_range text,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_campaignperformance OWNER TO postgres;

--
-- Name: deelflow_campaignperformance_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_campaignperformance_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_campaignperformance_id_seq OWNER TO postgres;

--
-- Name: deelflow_campaignperformance_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_campaignperformance_id_seq OWNED BY public.deelflow_campaignperformance.id;


--
-- Name: deelflow_campaignpropertystats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_campaignpropertystats (
    id bigint NOT NULL,
    total_properties bigint,
    distressed_properties bigint,
    competition_level text,
    avg_roi numeric,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_campaignpropertystats OWNER TO postgres;

--
-- Name: deelflow_campaignpropertystats_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_campaignpropertystats_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_campaignpropertystats_id_seq OWNER TO postgres;

--
-- Name: deelflow_campaignpropertystats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_campaignpropertystats_id_seq OWNED BY public.deelflow_campaignpropertystats.id;


--
-- Name: deelflow_campaignrecipient; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_campaignrecipient (
    id bigint NOT NULL,
    status text,
    response text,
    sent_at timestamp with time zone,
    campaign_id bigint,
    lead_id bigint
);


ALTER TABLE public.deelflow_campaignrecipient OWNER TO postgres;

--
-- Name: deelflow_campaignrecipient_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_campaignrecipient_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_campaignrecipient_id_seq OWNER TO postgres;

--
-- Name: deelflow_campaignrecipient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_campaignrecipient_id_seq OWNED BY public.deelflow_campaignrecipient.id;


--
-- Name: deelflow_channel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_channel (
    id bigint NOT NULL,
    name text,
    active boolean,
    created_at timestamp with time zone
);


ALTER TABLE public.deelflow_channel OWNER TO postgres;

--
-- Name: deelflow_channel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_channel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_channel_id_seq OWNER TO postgres;

--
-- Name: deelflow_channel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_channel_id_seq OWNED BY public.deelflow_channel.id;


--
-- Name: deelflow_channelresponserate; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_channelresponserate (
    id bigint NOT NULL,
    channel_name text,
    response_rate numeric,
    date_range text,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_channelresponserate OWNER TO postgres;

--
-- Name: deelflow_channelresponserate_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_channelresponserate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_channelresponserate_id_seq OWNER TO postgres;

--
-- Name: deelflow_channelresponserate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_channelresponserate_id_seq OWNED BY public.deelflow_channelresponserate.id;


--
-- Name: deelflow_compliancestatus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_compliancestatus (
    id bigint NOT NULL,
    compliance_percent numeric,
    audit_trail text,
    system_health text,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_compliancestatus OWNER TO postgres;

--
-- Name: deelflow_compliancestatus_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_compliancestatus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_compliancestatus_id_seq OWNER TO postgres;

--
-- Name: deelflow_compliancestatus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_compliancestatus_id_seq OWNED BY public.deelflow_compliancestatus.id;


--
-- Name: deelflow_discoveredlead; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_discoveredlead (
    id bigint NOT NULL,
    owner_name text,
    address text,
    city text,
    state text,
    zipcode text,
    source text,
    details text,
    motivation_score real,
    property_condition text,
    financial_situation text,
    timeline_urgency text,
    negotiation_style text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_discoveredlead OWNER TO postgres;

--
-- Name: deelflow_discoveredlead_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_discoveredlead_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_discoveredlead_id_seq OWNER TO postgres;

--
-- Name: deelflow_discoveredlead_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_discoveredlead_id_seq OWNED BY public.deelflow_discoveredlead.id;


--
-- Name: deelflow_historicalmetrics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_historicalmetrics (
    id bigint NOT NULL,
    metric_type text,
    metric_value numeric,
    record_date date
);


ALTER TABLE public.deelflow_historicalmetrics OWNER TO postgres;

--
-- Name: deelflow_historicalmetrics_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_historicalmetrics_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_historicalmetrics_id_seq OWNER TO postgres;

--
-- Name: deelflow_historicalmetrics_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_historicalmetrics_id_seq OWNED BY public.deelflow_historicalmetrics.id;


--
-- Name: deelflow_lead; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_lead (
    id bigint NOT NULL,
    status text,
    responded boolean,
    created_at timestamp with time zone,
    campaign_id bigint
);


ALTER TABLE public.deelflow_lead OWNER TO postgres;

--
-- Name: deelflow_lead_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_lead_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_lead_id_seq OWNER TO postgres;

--
-- Name: deelflow_lead_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_lead_id_seq OWNED BY public.deelflow_lead.id;


--
-- Name: deelflow_nlpprocessingmetrics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_nlpprocessingmetrics (
    id bigint NOT NULL,
    total_processed bigint,
    accuracy_rate real,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_nlpprocessingmetrics OWNER TO postgres;

--
-- Name: deelflow_nlpprocessingmetrics_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_nlpprocessingmetrics_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_nlpprocessingmetrics_id_seq OWNER TO postgres;

--
-- Name: deelflow_nlpprocessingmetrics_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_nlpprocessingmetrics_id_seq OWNED BY public.deelflow_nlpprocessingmetrics.id;


--
-- Name: deelflow_organization; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_organization (
    id bigint NOT NULL,
    uuid text,
    name text,
    slug text,
    subscription_status text,
    updated_at timestamp with time zone,
    created_at timestamp with time zone
);


ALTER TABLE public.deelflow_organization OWNER TO postgres;

--
-- Name: deelflow_organization_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_organization_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_organization_id_seq OWNER TO postgres;

--
-- Name: deelflow_organization_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_organization_id_seq OWNED BY public.deelflow_organization.id;


--
-- Name: deelflow_outreachcampaign; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_outreachcampaign (
    id bigint NOT NULL,
    name text,
    description text,
    channel text,
    message_template text,
    scheduled_time timestamp with time zone,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_outreachcampaign OWNER TO postgres;

--
-- Name: deelflow_outreachcampaign_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_outreachcampaign_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_outreachcampaign_id_seq OWNER TO postgres;

--
-- Name: deelflow_outreachcampaign_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_outreachcampaign_id_seq OWNED BY public.deelflow_outreachcampaign.id;


--
-- Name: deelflow_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_permission (
    id bigint NOT NULL,
    name text,
    label text
);


ALTER TABLE public.deelflow_permission OWNER TO postgres;

--
-- Name: deelflow_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_permission_id_seq OWNER TO postgres;

--
-- Name: deelflow_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_permission_id_seq OWNED BY public.deelflow_permission.id;


--
-- Name: deelflow_propertyaianalysis; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_propertyaianalysis (
    id bigint NOT NULL,
    address text,
    ai_confidence real,
    distress_level real,
    motivation text,
    timeline text,
    roi_percent real,
    cap_rate real,
    cash_flow real,
    market_stability_score real,
    comparables_confidence real,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_propertyaianalysis OWNER TO postgres;

--
-- Name: deelflow_propertyaianalysis_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_propertyaianalysis_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_propertyaianalysis_id_seq OWNER TO postgres;

--
-- Name: deelflow_propertyaianalysis_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_propertyaianalysis_id_seq OWNED BY public.deelflow_propertyaianalysis.id;


--
-- Name: deelflow_role; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_role (
    id bigint NOT NULL,
    name text,
    label text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_role OWNER TO postgres;

--
-- Name: deelflow_role_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_role_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_role_id_seq OWNER TO postgres;

--
-- Name: deelflow_role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_role_id_seq OWNED BY public.deelflow_role.id;


--
-- Name: deelflow_role_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_role_permissions (
    id bigint NOT NULL,
    role_id bigint,
    permission_id bigint
);


ALTER TABLE public.deelflow_role_permissions OWNER TO postgres;

--
-- Name: deelflow_role_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_role_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_role_permissions_id_seq OWNER TO postgres;

--
-- Name: deelflow_role_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_role_permissions_id_seq OWNED BY public.deelflow_role_permissions.id;


--
-- Name: deelflow_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_user (
    id bigint NOT NULL,
    uuid text,
    email text,
    first_name text,
    last_name text,
    phone text,
    role text,
    level bigint,
    points bigint,
    is_verified boolean,
    is_active boolean,
    stripe_customer_id text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    organization_id bigint,
    password text
);


ALTER TABLE public.deelflow_user OWNER TO postgres;

--
-- Name: deelflow_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_user_id_seq OWNER TO postgres;

--
-- Name: deelflow_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_user_id_seq OWNED BY public.deelflow_user.id;


--
-- Name: deelflow_visionanalysismetrics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_visionanalysismetrics (
    id bigint NOT NULL,
    total_analyses bigint,
    accuracy_rate real,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_visionanalysismetrics OWNER TO postgres;

--
-- Name: deelflow_visionanalysismetrics_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_visionanalysismetrics_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_visionanalysismetrics_id_seq OWNER TO postgres;

--
-- Name: deelflow_visionanalysismetrics_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_visionanalysismetrics_id_seq OWNED BY public.deelflow_visionanalysismetrics.id;


--
-- Name: deelflow_voiceaicallmetrics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deelflow_voiceaicallmetrics (
    id bigint NOT NULL,
    total_calls bigint,
    success_rate real,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);


ALTER TABLE public.deelflow_voiceaicallmetrics OWNER TO postgres;

--
-- Name: deelflow_voiceaicallmetrics_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deelflow_voiceaicallmetrics_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deelflow_voiceaicallmetrics_id_seq OWNER TO postgres;

--
-- Name: deelflow_voiceaicallmetrics_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deelflow_voiceaicallmetrics_id_seq OWNED BY public.deelflow_voiceaicallmetrics.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id bigint NOT NULL,
    object_id text,
    object_repr text,
    action_flag smallint,
    change_message text,
    content_type_id bigint,
    user_id bigint,
    action_time timestamp with time zone
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id bigint NOT NULL,
    app_label text,
    model text
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app text,
    name text,
    applied timestamp with time zone
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key text NOT NULL,
    session_data text,
    expire_date timestamp with time zone
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: deelflow_activityfeed id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_activityfeed ALTER COLUMN id SET DEFAULT nextval('public.deelflow_activityfeed_id_seq'::regclass);


--
-- Name: deelflow_blockchaintxnmetrics id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_blockchaintxnmetrics ALTER COLUMN id SET DEFAULT nextval('public.deelflow_blockchaintxnmetrics_id_seq'::regclass);


--
-- Name: deelflow_businessmetrics id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_businessmetrics ALTER COLUMN id SET DEFAULT nextval('public.deelflow_businessmetrics_id_seq'::regclass);


--
-- Name: deelflow_campaign id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_campaign ALTER COLUMN id SET DEFAULT nextval('public.deelflow_campaign_id_seq'::regclass);


--
-- Name: deelflow_campaignperformance id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_campaignperformance ALTER COLUMN id SET DEFAULT nextval('public.deelflow_campaignperformance_id_seq'::regclass);


--
-- Name: deelflow_campaignpropertystats id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_campaignpropertystats ALTER COLUMN id SET DEFAULT nextval('public.deelflow_campaignpropertystats_id_seq'::regclass);


--
-- Name: deelflow_campaignrecipient id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_campaignrecipient ALTER COLUMN id SET DEFAULT nextval('public.deelflow_campaignrecipient_id_seq'::regclass);


--
-- Name: deelflow_channel id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_channel ALTER COLUMN id SET DEFAULT nextval('public.deelflow_channel_id_seq'::regclass);


--
-- Name: deelflow_channelresponserate id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_channelresponserate ALTER COLUMN id SET DEFAULT nextval('public.deelflow_channelresponserate_id_seq'::regclass);


--
-- Name: deelflow_compliancestatus id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_compliancestatus ALTER COLUMN id SET DEFAULT nextval('public.deelflow_compliancestatus_id_seq'::regclass);


--
-- Name: deelflow_discoveredlead id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_discoveredlead ALTER COLUMN id SET DEFAULT nextval('public.deelflow_discoveredlead_id_seq'::regclass);


--
-- Name: deelflow_historicalmetrics id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_historicalmetrics ALTER COLUMN id SET DEFAULT nextval('public.deelflow_historicalmetrics_id_seq'::regclass);


--
-- Name: deelflow_lead id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_lead ALTER COLUMN id SET DEFAULT nextval('public.deelflow_lead_id_seq'::regclass);


--
-- Name: deelflow_nlpprocessingmetrics id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_nlpprocessingmetrics ALTER COLUMN id SET DEFAULT nextval('public.deelflow_nlpprocessingmetrics_id_seq'::regclass);


--
-- Name: deelflow_organization id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_organization ALTER COLUMN id SET DEFAULT nextval('public.deelflow_organization_id_seq'::regclass);


--
-- Name: deelflow_outreachcampaign id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_outreachcampaign ALTER COLUMN id SET DEFAULT nextval('public.deelflow_outreachcampaign_id_seq'::regclass);


--
-- Name: deelflow_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_permission ALTER COLUMN id SET DEFAULT nextval('public.deelflow_permission_id_seq'::regclass);


--
-- Name: deelflow_propertyaianalysis id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_propertyaianalysis ALTER COLUMN id SET DEFAULT nextval('public.deelflow_propertyaianalysis_id_seq'::regclass);


--
-- Name: deelflow_role id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_role ALTER COLUMN id SET DEFAULT nextval('public.deelflow_role_id_seq'::regclass);


--
-- Name: deelflow_role_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_role_permissions ALTER COLUMN id SET DEFAULT nextval('public.deelflow_role_permissions_id_seq'::regclass);


--
-- Name: deelflow_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_user ALTER COLUMN id SET DEFAULT nextval('public.deelflow_user_id_seq'::regclass);


--
-- Name: deelflow_visionanalysismetrics id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_visionanalysismetrics ALTER COLUMN id SET DEFAULT nextval('public.deelflow_visionanalysismetrics_id_seq'::regclass);


--
-- Name: deelflow_voiceaicallmetrics id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_voiceaicallmetrics ALTER COLUMN id SET DEFAULT nextval('public.deelflow_voiceaicallmetrics_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, content_type_id, codename, name) FROM stdin;
1	1	add_logentry	Can add log entry
2	1	change_logentry	Can change log entry
3	1	delete_logentry	Can delete log entry
4	1	view_logentry	Can view log entry
5	2	add_permission	Can add permission
6	2	change_permission	Can change permission
7	2	delete_permission	Can delete permission
8	2	view_permission	Can view permission
9	3	add_group	Can add group
10	3	change_group	Can change group
11	3	delete_group	Can delete group
12	3	view_group	Can view group
13	4	add_user	Can add user
14	4	change_user	Can change user
15	4	delete_user	Can delete user
16	4	view_user	Can view user
17	5	add_contenttype	Can add content type
18	5	change_contenttype	Can change content type
19	5	delete_contenttype	Can delete content type
20	5	view_contenttype	Can view content type
21	6	add_session	Can add session
22	6	change_session	Can change session
23	6	delete_session	Can delete session
24	6	view_session	Can view session
25	7	add_activityfeed	Can add activity feed
26	7	change_activityfeed	Can change activity feed
27	7	delete_activityfeed	Can delete activity feed
28	7	view_activityfeed	Can view activity feed
29	8	add_businessmetrics	Can add business metrics
30	8	change_businessmetrics	Can change business metrics
31	8	delete_businessmetrics	Can delete business metrics
32	8	view_businessmetrics	Can view business metrics
33	9	add_compliancestatus	Can add compliance status
34	9	change_compliancestatus	Can change compliance status
35	9	delete_compliancestatus	Can delete compliance status
36	9	view_compliancestatus	Can view compliance status
37	10	add_historicalmetrics	Can add historical metrics
38	10	change_historicalmetrics	Can change historical metrics
39	10	delete_historicalmetrics	Can delete historical metrics
40	10	view_historicalmetrics	Can view historical metrics
41	11	add_user	Can add user
42	11	change_user	Can change user
43	11	delete_user	Can delete user
44	11	view_user	Can view user
45	12	add_organization	Can add organization
46	12	change_organization	Can change organization
47	12	delete_organization	Can delete organization
48	12	view_organization	Can view organization
49	13	add_role	Can add role
50	13	change_role	Can change role
51	13	delete_role	Can delete role
52	13	view_role	Can view role
53	14	add_permission	Can add permission
54	14	change_permission	Can change permission
55	14	delete_permission	Can delete permission
56	14	view_permission	Can view permission
57	15	add_propertyaianalysis	Can add property ai analysis
58	15	change_propertyaianalysis	Can change property ai analysis
59	15	delete_propertyaianalysis	Can delete property ai analysis
60	15	view_propertyaianalysis	Can view property ai analysis
61	16	add_visionanalysismetrics	Can add vision analysis metrics
62	16	change_visionanalysismetrics	Can change vision analysis metrics
63	16	delete_visionanalysismetrics	Can delete vision analysis metrics
64	16	view_visionanalysismetrics	Can view vision analysis metrics
65	17	add_voiceaicallmetrics	Can add voice ai call metrics
66	17	change_voiceaicallmetrics	Can change voice ai call metrics
67	17	delete_voiceaicallmetrics	Can delete voice ai call metrics
68	17	view_voiceaicallmetrics	Can view voice ai call metrics
69	18	add_blockchaintxnmetrics	Can add blockchain txn metrics
70	18	change_blockchaintxnmetrics	Can change blockchain txn metrics
71	18	delete_blockchaintxnmetrics	Can delete blockchain txn metrics
72	18	view_blockchaintxnmetrics	Can view blockchain txn metrics
73	19	add_nlpprocessingmetrics	Can add nlp processing metrics
74	19	change_nlpprocessingmetrics	Can change nlp processing metrics
75	19	delete_nlpprocessingmetrics	Can delete nlp processing metrics
76	19	view_nlpprocessingmetrics	Can view nlp processing metrics
77	20	add_campaignperformance	Can add campaign performance
78	20	change_campaignperformance	Can change campaign performance
79	20	delete_campaignperformance	Can delete campaign performance
80	20	view_campaignperformance	Can view campaign performance
81	21	add_campaignpropertystats	Can add campaign property stats
82	21	change_campaignpropertystats	Can change campaign property stats
83	21	delete_campaignpropertystats	Can delete campaign property stats
84	21	view_campaignpropertystats	Can view campaign property stats
85	22	add_channel	Can add channel
86	22	change_channel	Can change channel
87	22	delete_channel	Can delete channel
88	22	view_channel	Can view channel
89	23	add_channelresponserate	Can add channel response rate
90	23	change_channelresponserate	Can change channel response rate
91	23	delete_channelresponserate	Can delete channel response rate
92	23	view_channelresponserate	Can view channel response rate
93	24	add_lead	Can add lead
94	24	change_lead	Can change lead
95	24	delete_lead	Can delete lead
96	24	view_lead	Can view lead
97	25	add_campaign	Can add campaign
98	25	change_campaign	Can change campaign
99	25	delete_campaign	Can delete campaign
100	25	view_campaign	Can view campaign
101	26	add_discoveredlead	Can add discovered lead
102	26	change_discoveredlead	Can change discovered lead
103	26	delete_discoveredlead	Can delete discovered lead
104	26	view_discoveredlead	Can view discovered lead
105	27	add_outreachcampaign	Can add outreach campaign
106	27	change_outreachcampaign	Can change outreach campaign
107	27	delete_outreachcampaign	Can delete outreach campaign
108	27	view_outreachcampaign	Can view outreach campaign
109	28	add_campaignrecipient	Can add campaign recipient
110	28	change_campaignrecipient	Can change campaign recipient
111	28	delete_campaignrecipient	Can delete campaign recipient
112	28	view_campaignrecipient	Can view campaign recipient
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) FROM stdin;
1	pbkdf2_sha256$600000$Ag2xbqCPj7xNFQFzeXpq1l$eB4Fk87xnzspQa0ntRcL7cieds5V72ft5hMuOYy6vO0=	2025-09-22 08:56:06.701174+00	t	deelflow2025		arpan.s@vycentra.com	t	t	2025-08-25 10:25:13.899988+00	
2	pbkdf2_sha256$600000$NIihh0XYakej9bOIkF3zzj$S+mM7uEJd3TF/zLkRqR98uEIPMZga0mYEjyhb/kdmJ0=	\N	f	arpan58	Sarkar		f	t	2025-08-29 13:05:33+00	Arpan
3	pbkdf2_sha256$600000$DtL8ZdRHLNV5JJ0dpSJTMv$ohPW0QWyLoxcDc1WGOfoI3kWn+ZuwG4H9DGsLSNhH0Q=	\N	t	arpans05		arpansarkar@vrxlab.com	t	t	2025-09-01 11:34:31.402456+00	
4	pbkdf2_sha256$600000$r3HfqhIIh8LKzX7xClZGOg$SqVpMFpttxBrTr9gZCSR1/+XSHpCSeFnwcwSS2wzp/Y=	\N	t	arpans		arpansarkar@vrxlab.com	t	t	2025-09-01 11:44:32.592322+00	
5	pbkdf2_sha256$600000$jtwiPbzQflCI8oRpqepuOS$QpDxhzoaAFW8C6J6/mXF+MR0FtEKkodKQxP/C7Es15E=	2025-09-15 16:57:27.527262+00	t	Anirudha007		anirudha.das2551995@gmail.com	t	t	2025-09-09 14:19:09.017706+00	
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: deelflow_activityfeed; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_activityfeed (id, user_id, action_type, description, "timestamp") FROM stdin;
1	0	Malware	Rachel W., David M. activities	2025-08-25 10:35:43.953288+00
2	1	Ransomware	Arpan S., Anirudha M. activities	2025-08-25 10:37:21.789413+00
\.


--
-- Data for Name: deelflow_blockchaintxnmetrics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_blockchaintxnmetrics (id, total_txns, success_rate, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: deelflow_businessmetrics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_businessmetrics (id, total_revenue, active_users, properties_listed, total_deals, monthly_profit, voice_calls_count, report_date, ai_conversations) FROM stdin;
1	4.35	14238	3847	47	127500	89	2025-08-25	48.2
\.


--
-- Data for Name: deelflow_campaign; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_campaign (id, name, status, created_at, budget, campaign_type, channel, distress_indicators, email_content, geographic_scope_type, geographic_scope_values, location, max_price, min_price, minimum_equity, property_type, scheduled_at, subject_line, use_ai_personalization) FROM stdin;
1	test	active	2025-09-15 18:01:00.288269+00	\N	new	email	[]	\N	zip	[]	\N	\N	\N	\N	\N	\N	\N	f
2	Summer Sale Campaign	active	2025-09-22 08:55:18.469285+00	5000	new	email	['Pre-foreclosure', 'Tax Liens']	Hello! Check out our special summer deals on properties in your area.	zip	['33101', '33102', '33103']	Miami	750000	250000	100000	Residential	2025-09-25 10:00:00+00	Exclusive Summer Deals for Your Property!	t
3	IP List	inactive	2025-09-23 13:04:53.488742+00	1000	seller_finder	sms	['Tax Liens']	safrtw4e	zip	4354	tre	31	18	21	est	2025-09-08 15:08:00+00	rtyr	t
\.


--
-- Data for Name: deelflow_campaignperformance; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_campaignperformance (id, campaign_type, roi_percentage, date_range, updated_at) FROM stdin;
\.


--
-- Data for Name: deelflow_campaignpropertystats; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_campaignpropertystats (id, total_properties, distressed_properties, competition_level, avg_roi, updated_at) FROM stdin;
\.


--
-- Data for Name: deelflow_campaignrecipient; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_campaignrecipient (id, status, response, sent_at, campaign_id, lead_id) FROM stdin;
\.


--
-- Data for Name: deelflow_channel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_channel (id, name, active, created_at) FROM stdin;
\.


--
-- Data for Name: deelflow_channelresponserate; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_channelresponserate (id, channel_name, response_rate, date_range, updated_at) FROM stdin;
\.


--
-- Data for Name: deelflow_compliancestatus; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_compliancestatus (id, compliance_percent, audit_trail, system_health, updated_at) FROM stdin;
1	96	ADMIN: Login successful\r\nJANE.DOE: Login failed (wrong password)\r\nKYC: Customer ID #102 verified\r\nSYSTEM: Health status updated to Healthy	89.55%	2025-08-25 10:44:22.712762+00
\.


--
-- Data for Name: deelflow_discoveredlead; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_discoveredlead (id, owner_name, address, city, state, zipcode, source, details, motivation_score, property_condition, financial_situation, timeline_urgency, negotiation_style, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: deelflow_historicalmetrics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_historicalmetrics (id, metric_type, metric_value, record_date) FROM stdin;
1	new signups	4508	2025-08-25
\.


--
-- Data for Name: deelflow_lead; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_lead (id, status, responded, created_at, campaign_id) FROM stdin;
1	qualified	t	2025-09-15 18:01:05.187117+00	1
\.


--
-- Data for Name: deelflow_nlpprocessingmetrics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_nlpprocessingmetrics (id, total_processed, accuracy_rate, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: deelflow_organization; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_organization (id, uuid, name, slug, subscription_status, updated_at, created_at) FROM stdin;
1	bdc653918f284fbf81f792414f4fca33	test admin org	test-admin-org	new	2025-09-04 06:05:36.501889+00	2025-09-04 06:05:36.501889+00
3	0d24147a168d4426bf1fd7c3b1f427b0	test admin org	test-arpan-org	new	2025-09-04 06:26:03.33916+00	2025-09-04 06:26:03.33916+00
4	9f287ac6330c42519fbe5c3b036a5f27	Wipro	Wipro	new	2025-09-09 14:29:48.951318+00	2025-09-09 14:29:48.951318+00
5	2c43265273d34ac3b2383c73679fe4e5	goodcausesolutions	goodcausesolutions	new	2025-09-15 05:42:17.101117+00	2025-09-15 05:42:17.101117+00
6	9b5b921a80b14a6292a797fde910a288	vcentra	vcentra	new	2025-09-15 16:54:24.519953+00	2025-09-15 16:54:24.519953+00
7	9634f6cc68924e83a563dca8c0763e62	test super admin org	super_admin-garth-org	new	2025-09-22 08:56:38.806026+00	2025-09-22 08:56:38.806026+00
\.


--
-- Data for Name: deelflow_outreachcampaign; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_outreachcampaign (id, name, description, channel, message_template, scheduled_time, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: deelflow_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_permission (id, name, label) FROM stdin;
1	manage_roles	Manage Roles
2	manage_client	Manage Clients
3	manage_campaign	Manage Campaigns
4	manage_org	Manage Organization
5	manage_lead	Manage Leads
6	manage_properties	Manage Properties
\.


--
-- Data for Name: deelflow_propertyaianalysis; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_propertyaianalysis (id, address, ai_confidence, distress_level, motivation, timeline, roi_percent, cap_rate, cash_flow, market_stability_score, comparables_confidence, created_at, updated_at) FROM stdin;
1	1247 Oak Street, Dallas, TX 75201	58	8.5	High – Divorce Settlement	30–45 days	12.7	6.2	540	7.2	90	2025-09-09 17:43:43.747322+00	2025-09-19 01:21:03.091215+00
\.


--
-- Data for Name: deelflow_role; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_role (id, name, label, created_at, updated_at) FROM stdin;
1	manager	Manager	2025-09-09 04:00:03.462405+00	2025-09-22 08:43:29.554178+00
2	Arpan	admin	2025-09-22 10:35:18.357134+00	2025-09-22 10:35:18.364634+00
3	Anirudha	admin	2025-09-22 10:42:26.098015+00	2025-09-22 10:42:26.102884+00
4	Abhishek	admin	2025-09-22 10:48:05.325229+00	2025-09-22 10:48:05.495331+00
\.


--
-- Data for Name: deelflow_role_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_role_permissions (id, role_id, permission_id) FROM stdin;
1	4	1
2	4	3
\.


--
-- Data for Name: deelflow_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_user (id, uuid, email, first_name, last_name, phone, role, level, points, is_verified, is_active, stripe_customer_id, created_at, updated_at, organization_id, password) FROM stdin;
1	bbd013ae86224521bf064d8a7aacadcf	admin@gmail.com	admin	admin	1234567890	admin	1	0	f	t	cus_SrKt16siewODxX	2025-09-04 06:05:36.94116+00	2025-09-04 06:05:36.94116+00	1	1992
3	42231c5f2e694d4abb64e4f63749a64f	arpansarkar@gmail.com	admin	admin	1234567890	admin	1	0	f	t	cus_SrKt16siewODxX	2025-09-04 06:26:03.776744+00	2025-09-04 06:26:03.776744+00	3	pbkdf2_sha256$600000$LJ9cZHmHEt5wvBvlQN2TdY$UwFRH0ZBub3GxqrCbycBJSdrx6K6un/23x1xXfDuCkE=
4	1beddf3f43814d958f944865020050c5	bappa.anirudha@gmail.com	Anirudha2	Das	7908934723	staff	1	0	f	t	\N	2025-09-09 14:29:48.961001+00	2025-09-09 14:29:48.961001+00	4	pbkdf2_sha256$600000$Mcbep4mf88tlAqhAM8o3bw$PUicaWhU5dxcjJZW5EtE4fFZ884XSi1tzCjLIBEZps8=
5	9564a304de5f4bb6bee8954e52447c4b	tridha@gmail.com	Tridha	Das	8845678334	staff	1	0	f	t	\N	2025-09-15 05:42:17.122282+00	2025-09-15 05:42:17.122282+00	5	pbkdf2_sha256$600000$dPQ7dzdFf6CiBRKHOILfpX$O1UvdXlCj/rZGBPT5eRBEiyKI7E8TCTW6NTpC1d8Rhs=
6	b239500f777c49c198746fc937484b30	info@vcentra.com	clive	garth	9800000000	staff	1	0	f	t	\N	2025-09-15 16:54:24.528757+00	2025-09-15 16:54:24.528757+00	6	pbkdf2_sha256$600000$SrnYwCyPFfMdcn1NNOVYNl$AJ+ZSp0Jv4sX1ymz4BL9Wc6FEREs4+qZaNNRgQqHN4A=
7	c48875a271714736b742c602df6816f9	abhishake@gmail.com	Abhishake	Saha	09800000000	user	1	0	f	t	\N	2025-09-15 17:02:58.98705+00	2025-09-15 17:02:58.98705+00	4	vcentra@123
8	2bde730d8b054f1da452d76d752fbc04	garthsmith@vycentra.com	Garth	Smith	1234567890	super admin	1	0	f	t	cus_SrKt16siewODxX	2025-09-22 08:56:39.243184+00	2025-09-22 08:56:39.243184+00	7	pbkdf2_sha256$600000$0lrQSIWrkzhc8C2ZM4cSdR$h6thQL2GiUOZv/xwKsdX4EZKEpwgd6b+bepyD4DQJKs=
\.


--
-- Data for Name: deelflow_visionanalysismetrics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_visionanalysismetrics (id, total_analyses, accuracy_rate, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: deelflow_voiceaicallmetrics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deelflow_voiceaicallmetrics (id, total_calls, success_rate, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, object_id, object_repr, action_flag, change_message, content_type_id, user_id, action_time) FROM stdin;
1	1	Malware by 0 at 2025-08-25 10:35:43.953288+00:00	1	[{"added": {}}]	7	1	2025-08-25 10:35:43.959104+00
2	2	Ransomware by 1 at 2025-08-25 10:37:21.789413+00:00	1	[{"added": {}}]	7	1	2025-08-25 10:37:21.792926+00
3	1	Metrics on 2025-08-25	1	[{"added": {}}]	8	1	2025-08-25 10:40:57.786759+00
4	1	Metrics on 2025-08-25	2	[]	8	1	2025-08-25 10:41:36.298803+00
5	1	Compliance 96% (89.55%)	1	[{"added": {}}]	9	1	2025-08-25 10:44:22.718149+00
6	1	new_signups - 2025-08-25	1	[{"added": {}}]	10	1	2025-08-25 10:53:10.415313+00
7	1	new signups - 2025-08-25	2	[{"changed": {"fields": ["Metric type"]}}]	10	1	2025-08-25 10:53:20.875103+00
8	2	arpan58	1	[{"added": {}}]	4	1	2025-08-29 13:05:33.588794+00
9	2	arpan58	2	[{"changed": {"fields": ["First name", "Last name"]}}]	4	1	2025-08-29 13:05:55.986778+00
10	2	admin admin (arpansarkar@gmail.com)	3		11	1	2025-09-04 06:24:08.760957+00
11	2	test admin org	3		12	1	2025-09-04 06:24:17.506585+00
12	1	Metrics on 2025-08-25	2	[{"changed": {"fields": ["Total revenue"]}}]	8	5	2025-09-15 16:57:50.86663+00
13	7	Abhishake Saha (abhishake@gmail.com)	1	[{"added": {}}]	11	5	2025-09-15 17:02:58.990986+00
14	1	test	1	[{"added": {}}]	25	5	2025-09-15 18:01:00.293076+00
15	1	Lead 1 - qualified	1	[{"added": {}}]	24	5	2025-09-15 18:01:05.188119+00
16	1	Manage Roles	1	[{"added": {}}]	14	1	2025-09-22 10:43:49.721028+00
17	2	Manage Clients	1	[{"added": {}}]	14	1	2025-09-22 10:44:11.835561+00
18	3	Manage Campaigns	1	[{"added": {}}]	14	1	2025-09-22 10:44:35.705178+00
19	4	Manage Organization	1	[{"added": {}}]	14	1	2025-09-22 10:45:05.205469+00
20	5	Manage Leads	1	[{"added": {}}]	14	1	2025-09-22 10:45:21.956173+00
21	6	Manage Properties	1	[{"added": {}}]	14	1	2025-09-22 10:45:36.999335+00
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	deelflow	activityfeed
8	deelflow	businessmetrics
9	deelflow	compliancestatus
10	deelflow	historicalmetrics
11	deelflow	user
12	deelflow	organization
13	deelflow	role
14	deelflow	permission
15	deelflow	propertyaianalysis
16	deelflow	visionanalysismetrics
17	deelflow	voiceaicallmetrics
18	deelflow	blockchaintxnmetrics
19	deelflow	nlpprocessingmetrics
20	deelflow	campaignperformance
21	deelflow	campaignpropertystats
22	deelflow	channel
23	deelflow	channelresponserate
24	deelflow	lead
25	deelflow	campaign
26	deelflow	discoveredlead
27	deelflow	outreachcampaign
28	deelflow	campaignrecipient
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2025-08-25 10:22:53.773375+00
2	auth	0001_initial	2025-08-25 10:22:53.869133+00
3	admin	0001_initial	2025-08-25 10:22:53.949764+00
4	admin	0002_logentry_remove_auto_add	2025-08-25 10:22:54.007108+00
5	admin	0003_logentry_add_action_flag_choices	2025-08-25 10:22:54.056378+00
6	contenttypes	0002_remove_content_type_name	2025-08-25 10:22:54.113436+00
7	auth	0002_alter_permission_name_max_length	2025-08-25 10:22:54.166238+00
8	auth	0003_alter_user_email_max_length	2025-08-25 10:22:54.221789+00
9	auth	0004_alter_user_username_opts	2025-08-25 10:22:54.264321+00
10	auth	0005_alter_user_last_login_null	2025-08-25 10:22:54.314825+00
11	auth	0006_require_contenttypes_0002	2025-08-25 10:22:54.349913+00
12	auth	0007_alter_validators_add_error_messages	2025-08-25 10:22:54.400138+00
13	auth	0008_alter_user_username_max_length	2025-08-25 10:22:54.449801+00
14	auth	0009_alter_user_last_name_max_length	2025-08-25 10:22:54.512259+00
15	auth	0010_alter_group_name_max_length	2025-08-25 10:22:54.552126+00
16	auth	0011_update_proxy_permissions	2025-08-25 10:22:54.595361+00
17	auth	0012_alter_user_first_name_max_length	2025-08-25 10:22:54.646803+00
18	deelflow	0001_initial	2025-08-25 10:22:54.688324+00
19	sessions	0001_initial	2025-08-25 10:22:54.762205+00
20	deelflow	0002_alter_businessmetrics_ai_conversations	2025-08-25 10:40:44.796278+00
21	deelflow	0003_organization_user	2025-09-04 05:40:38.547409+00
22	deelflow	0004_user_password	2025-09-04 06:23:15.660951+00
23	deelflow	0005_permission_role	2025-09-08 03:45:09.0285+00
24	deelflow	0006_propertyaianalysis	2025-09-09 16:13:33.582019+00
25	deelflow	0007_visionanalysismetrics_voiceaicallmetrics	2025-09-09 17:57:20.113091+00
26	deelflow	0008_blockchaintxnmetrics_nlpprocessingmetrics	2025-09-09 18:00:48.949777+00
27	deelflow	0009_campaign_campaignperformance_campaignpropertystats_and_more	2025-09-10 07:47:45.084729+00
28	deelflow	0010_discoveredlead	2025-09-15 06:43:04.65589+00
29	deelflow	0011_outreachcampaign_campaignrecipient	2025-09-15 06:48:11.364081+00
30	deelflow	0012_remove_campaign_end_date_remove_campaign_start_date_and_more	2025-09-22 08:36:28.724291+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
bpqeyia61yrxo8hvq8husv1cyjorfcbj	.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1uqUP7:igABz19hoWoJVONB_e7mv_PMi7bq7YFBAHEae6LJl74	2025-09-08 10:26:21.632011+00
j0p9p7nqcs9lxld7kytlw5wlmh2eonxo	.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1utJwk:8RlFYrm8ZAMaCHmX6mAuOH_GAJmy7ului5s9vgopz_s	2025-09-16 05:52:46.010661+00
h3ug9hstf5s3rkzxjg45j1mqsl3mot89	.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1utMlk:m-BXlor8CMLUOo9aD9ziFOsRlM_o9Bu41m3CnLGGnBM	2025-09-16 08:53:36.976394+00
i2hjcpntrof7xpbash9o3n5gr08xtyta	.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1utpMI:DuLkCMRVs0WAp2I-xoXfSGMQsiGxcM1DbS_JG4G2_Eg	2025-09-17 15:25:14.59641+00
aaznsdw2d8l3p7h29x8gf9lek6xz8gg8	.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1uu2nx:LwyGIB3Wt1Z14ZE9Ntn7li1zQMO69SmxdvfmRNKdzYc	2025-09-18 05:46:41.827382+00
6zyxpyurvvc6nx8troiks0mp3pbdoflu	.eJxVjEEOwiAQRe_C2pDCQFtcuu8ZyMAMUjWQlHZlvLtt0oVu_3vvv4XHbc1-a7z4mcRVWHH53QLGJ5cD0APLvcpYy7rMQR6KPGmTUyV-3U737yBjy3udnDJWJ6vJBgygohvAUa-J0cUECTQEy5pHSggDs-5NBwZVp8a9MkZ8vu-bN9A:1uvzCG:2s6yKwakfmsWIx99ZBA_-NNM-OaDX9bV164j6VkxcAc	2025-09-23 14:19:48.700282+00
45c2pnzid3ybttfod681bffppayux2lj	.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1uwFWP:0m7R_VrcOq_hK3R6eqSSgLoVTGHEiyvkZXPvS30yGtw	2025-09-24 07:45:41.425061+00
zqlii61ke52szjmfsze8qtzo7kdtttyo	.eJxVjEEOwiAQRe_C2pDCQFtcuu8ZyMAMUjWQlHZlvLtt0oVu_3vvv4XHbc1-a7z4mcRVWHH53QLGJ5cD0APLvcpYy7rMQR6KPGmTUyV-3U737yBjy3udnDJWJ6vJBgygohvAUa-J0cUECTQEy5pHSggDs-5NBwZVp8a9MkZ8vu-bN9A:1uy23U:iZQ28XU4mySktQi6mZS9O14uzVQ7oQ0sE29Xcee9Vfc	2025-09-29 05:47:12.31986+00
4oauyv7oafw8d1sp3f5hvqrbzjxvs53j	.eJxVjEEOwiAQRe_C2pDCQFtcuu8ZyMAMUjWQlHZlvLtt0oVu_3vvv4XHbc1-a7z4mcRVWHH53QLGJ5cD0APLvcpYy7rMQR6KPGmTUyV-3U737yBjy3udnDJWJ6vJBgygohvAUa-J0cUECTQEy5pHSggDs-5NBwZVp8a9MkZ8vu-bN9A:1uyCW7:X-ho9Jgapve9JnnsiNO0dMvPqQc-D44xIE0LLeKAyWs	2025-09-29 16:57:27.53331+00
pkpurgf573bpv6t39k83hlgnsis77srs	.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1v0cL8:GtRoNHwviBDqtADk-y4qs6-f4olTM1SJEGYu0VQH6RI	2025-10-06 08:56:06.738158+00
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 112, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 5, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, true);


--
-- Name: deelflow_activityfeed_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_activityfeed_id_seq', 2, true);


--
-- Name: deelflow_blockchaintxnmetrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_blockchaintxnmetrics_id_seq', 1, true);


--
-- Name: deelflow_businessmetrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_businessmetrics_id_seq', 1, true);


--
-- Name: deelflow_campaign_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_campaign_id_seq', 3, true);


--
-- Name: deelflow_campaignperformance_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_campaignperformance_id_seq', 1, true);


--
-- Name: deelflow_campaignpropertystats_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_campaignpropertystats_id_seq', 1, true);


--
-- Name: deelflow_campaignrecipient_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_campaignrecipient_id_seq', 1, true);


--
-- Name: deelflow_channel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_channel_id_seq', 1, true);


--
-- Name: deelflow_channelresponserate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_channelresponserate_id_seq', 1, true);


--
-- Name: deelflow_compliancestatus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_compliancestatus_id_seq', 1, true);


--
-- Name: deelflow_discoveredlead_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_discoveredlead_id_seq', 1, true);


--
-- Name: deelflow_historicalmetrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_historicalmetrics_id_seq', 1, true);


--
-- Name: deelflow_lead_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_lead_id_seq', 1, true);


--
-- Name: deelflow_nlpprocessingmetrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_nlpprocessingmetrics_id_seq', 1, true);


--
-- Name: deelflow_organization_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_organization_id_seq', 7, true);


--
-- Name: deelflow_outreachcampaign_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_outreachcampaign_id_seq', 1, true);


--
-- Name: deelflow_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_permission_id_seq', 6, true);


--
-- Name: deelflow_propertyaianalysis_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_propertyaianalysis_id_seq', 1, true);


--
-- Name: deelflow_role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_role_id_seq', 4, true);


--
-- Name: deelflow_role_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_role_permissions_id_seq', 2, true);


--
-- Name: deelflow_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_user_id_seq', 8, true);


--
-- Name: deelflow_visionanalysismetrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_visionanalysismetrics_id_seq', 1, true);


--
-- Name: deelflow_voiceaicallmetrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deelflow_voiceaicallmetrics_id_seq', 1, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 21, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 28, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 30, true);


--
-- Name: django_migrations idx_16390_django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT idx_16390_django_migrations_pkey PRIMARY KEY (id);


--
-- Name: auth_group_permissions idx_16397_auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT idx_16397_auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups idx_16402_auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT idx_16402_auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions idx_16407_auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT idx_16407_auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log idx_16412_django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT idx_16412_django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type idx_16419_django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT idx_16419_django_content_type_pkey PRIMARY KEY (id);


--
-- Name: auth_permission idx_16426_auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT idx_16426_auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_group idx_16433_auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT idx_16433_auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_user idx_16440_auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT idx_16440_auth_user_pkey PRIMARY KEY (id);


--
-- Name: deelflow_activityfeed idx_16447_deelflow_activityfeed_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_activityfeed
    ADD CONSTRAINT idx_16447_deelflow_activityfeed_pkey PRIMARY KEY (id);


--
-- Name: deelflow_compliancestatus idx_16454_deelflow_compliancestatus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_compliancestatus
    ADD CONSTRAINT idx_16454_deelflow_compliancestatus_pkey PRIMARY KEY (id);


--
-- Name: deelflow_historicalmetrics idx_16461_deelflow_historicalmetrics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_historicalmetrics
    ADD CONSTRAINT idx_16461_deelflow_historicalmetrics_pkey PRIMARY KEY (id);


--
-- Name: django_session idx_16467_sqlite_autoindex_django_session_1; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT idx_16467_sqlite_autoindex_django_session_1 PRIMARY KEY (session_key);


--
-- Name: deelflow_businessmetrics idx_16473_deelflow_businessmetrics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_businessmetrics
    ADD CONSTRAINT idx_16473_deelflow_businessmetrics_pkey PRIMARY KEY (id);


--
-- Name: deelflow_organization idx_16480_deelflow_organization_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_organization
    ADD CONSTRAINT idx_16480_deelflow_organization_pkey PRIMARY KEY (id);


--
-- Name: deelflow_user idx_16487_deelflow_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_user
    ADD CONSTRAINT idx_16487_deelflow_user_pkey PRIMARY KEY (id);


--
-- Name: deelflow_permission idx_16494_deelflow_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_permission
    ADD CONSTRAINT idx_16494_deelflow_permission_pkey PRIMARY KEY (id);


--
-- Name: deelflow_role idx_16501_deelflow_role_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_role
    ADD CONSTRAINT idx_16501_deelflow_role_pkey PRIMARY KEY (id);


--
-- Name: deelflow_role_permissions idx_16508_deelflow_role_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_role_permissions
    ADD CONSTRAINT idx_16508_deelflow_role_permissions_pkey PRIMARY KEY (id);


--
-- Name: deelflow_propertyaianalysis idx_16513_deelflow_propertyaianalysis_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_propertyaianalysis
    ADD CONSTRAINT idx_16513_deelflow_propertyaianalysis_pkey PRIMARY KEY (id);


--
-- Name: deelflow_visionanalysismetrics idx_16520_deelflow_visionanalysismetrics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_visionanalysismetrics
    ADD CONSTRAINT idx_16520_deelflow_visionanalysismetrics_pkey PRIMARY KEY (id);


--
-- Name: deelflow_voiceaicallmetrics idx_16525_deelflow_voiceaicallmetrics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_voiceaicallmetrics
    ADD CONSTRAINT idx_16525_deelflow_voiceaicallmetrics_pkey PRIMARY KEY (id);


--
-- Name: deelflow_blockchaintxnmetrics idx_16530_deelflow_blockchaintxnmetrics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_blockchaintxnmetrics
    ADD CONSTRAINT idx_16530_deelflow_blockchaintxnmetrics_pkey PRIMARY KEY (id);


--
-- Name: deelflow_nlpprocessingmetrics idx_16535_deelflow_nlpprocessingmetrics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_nlpprocessingmetrics
    ADD CONSTRAINT idx_16535_deelflow_nlpprocessingmetrics_pkey PRIMARY KEY (id);


--
-- Name: deelflow_campaignperformance idx_16540_deelflow_campaignperformance_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_campaignperformance
    ADD CONSTRAINT idx_16540_deelflow_campaignperformance_pkey PRIMARY KEY (id);


--
-- Name: deelflow_campaignpropertystats idx_16547_deelflow_campaignpropertystats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_campaignpropertystats
    ADD CONSTRAINT idx_16547_deelflow_campaignpropertystats_pkey PRIMARY KEY (id);


--
-- Name: deelflow_channel idx_16554_deelflow_channel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_channel
    ADD CONSTRAINT idx_16554_deelflow_channel_pkey PRIMARY KEY (id);


--
-- Name: deelflow_channelresponserate idx_16561_deelflow_channelresponserate_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_channelresponserate
    ADD CONSTRAINT idx_16561_deelflow_channelresponserate_pkey PRIMARY KEY (id);


--
-- Name: deelflow_lead idx_16568_deelflow_lead_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_lead
    ADD CONSTRAINT idx_16568_deelflow_lead_pkey PRIMARY KEY (id);


--
-- Name: deelflow_discoveredlead idx_16575_deelflow_discoveredlead_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_discoveredlead
    ADD CONSTRAINT idx_16575_deelflow_discoveredlead_pkey PRIMARY KEY (id);


--
-- Name: deelflow_outreachcampaign idx_16582_deelflow_outreachcampaign_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_outreachcampaign
    ADD CONSTRAINT idx_16582_deelflow_outreachcampaign_pkey PRIMARY KEY (id);


--
-- Name: deelflow_campaignrecipient idx_16589_deelflow_campaignrecipient_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_campaignrecipient
    ADD CONSTRAINT idx_16589_deelflow_campaignrecipient_pkey PRIMARY KEY (id);


--
-- Name: deelflow_campaign idx_16596_deelflow_campaign_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_campaign
    ADD CONSTRAINT idx_16596_deelflow_campaign_pkey PRIMARY KEY (id);


--
-- Name: idx_16397_auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16397_auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: idx_16397_auth_group_permissions_group_id_permission_id_0cd325b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16397_auth_group_permissions_group_id_permission_id_0cd325b ON public.auth_group_permissions USING btree (group_id, permission_id);


--
-- Name: idx_16397_auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16397_auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: idx_16402_auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16402_auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: idx_16402_auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16402_auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: idx_16402_auth_user_groups_user_id_group_id_94350c0c_uniq; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16402_auth_user_groups_user_id_group_id_94350c0c_uniq ON public.auth_user_groups USING btree (user_id, group_id);


--
-- Name: idx_16407_auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16407_auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: idx_16407_auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16407_auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: idx_16407_auth_user_user_permissions_user_id_permission_id_14a6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16407_auth_user_user_permissions_user_id_permission_id_14a6 ON public.auth_user_user_permissions USING btree (user_id, permission_id);


--
-- Name: idx_16412_django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16412_django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: idx_16412_django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16412_django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: idx_16419_django_content_type_app_label_model_76bd3d3b_uniq; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16419_django_content_type_app_label_model_76bd3d3b_uniq ON public.django_content_type USING btree (app_label, model);


--
-- Name: idx_16426_auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16426_auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: idx_16426_auth_permission_content_type_id_codename_01ab375a_uni; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16426_auth_permission_content_type_id_codename_01ab375a_uni ON public.auth_permission USING btree (content_type_id, codename);


--
-- Name: idx_16433_sqlite_autoindex_auth_group_1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16433_sqlite_autoindex_auth_group_1 ON public.auth_group USING btree (name);


--
-- Name: idx_16440_sqlite_autoindex_auth_user_1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16440_sqlite_autoindex_auth_user_1 ON public.auth_user USING btree (username);


--
-- Name: idx_16467_django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16467_django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: idx_16480_sqlite_autoindex_deelflow_organization_1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16480_sqlite_autoindex_deelflow_organization_1 ON public.deelflow_organization USING btree (uuid);


--
-- Name: idx_16480_sqlite_autoindex_deelflow_organization_2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16480_sqlite_autoindex_deelflow_organization_2 ON public.deelflow_organization USING btree (slug);


--
-- Name: idx_16487_deelflow_user_organization_id_bdeea6b3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16487_deelflow_user_organization_id_bdeea6b3 ON public.deelflow_user USING btree (organization_id);


--
-- Name: idx_16487_sqlite_autoindex_deelflow_user_1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16487_sqlite_autoindex_deelflow_user_1 ON public.deelflow_user USING btree (uuid);


--
-- Name: idx_16487_sqlite_autoindex_deelflow_user_2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16487_sqlite_autoindex_deelflow_user_2 ON public.deelflow_user USING btree (email);


--
-- Name: idx_16494_sqlite_autoindex_deelflow_permission_1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16494_sqlite_autoindex_deelflow_permission_1 ON public.deelflow_permission USING btree (name);


--
-- Name: idx_16501_sqlite_autoindex_deelflow_role_1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16501_sqlite_autoindex_deelflow_role_1 ON public.deelflow_role USING btree (name);


--
-- Name: idx_16508_deelflow_role_permissions_permission_id_3cd4536b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16508_deelflow_role_permissions_permission_id_3cd4536b ON public.deelflow_role_permissions USING btree (permission_id);


--
-- Name: idx_16508_deelflow_role_permissions_role_id_f2265a76; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16508_deelflow_role_permissions_role_id_f2265a76 ON public.deelflow_role_permissions USING btree (role_id);


--
-- Name: idx_16508_deelflow_role_permissions_role_id_permission_id_d5db8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16508_deelflow_role_permissions_role_id_permission_id_d5db8 ON public.deelflow_role_permissions USING btree (role_id, permission_id);


--
-- Name: idx_16513_sqlite_autoindex_deelflow_propertyaianalysis_1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16513_sqlite_autoindex_deelflow_propertyaianalysis_1 ON public.deelflow_propertyaianalysis USING btree (address);


--
-- Name: idx_16554_sqlite_autoindex_deelflow_channel_1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16554_sqlite_autoindex_deelflow_channel_1 ON public.deelflow_channel USING btree (name);


--
-- Name: idx_16568_deelflow_lead_campaign_id_8e836f6e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16568_deelflow_lead_campaign_id_8e836f6e ON public.deelflow_lead USING btree (campaign_id);


--
-- Name: idx_16589_deelflow_campaignrecipient_campaign_id_f5a2b711; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16589_deelflow_campaignrecipient_campaign_id_f5a2b711 ON public.deelflow_campaignrecipient USING btree (campaign_id);


--
-- Name: idx_16589_deelflow_campaignrecipient_lead_id_cb28decc; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16589_deelflow_campaignrecipient_lead_id_cb28decc ON public.deelflow_campaignrecipient USING btree (lead_id);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.auth_group(id);


--
-- Name: auth_group_permissions auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id);


--
-- Name: auth_permission auth_permission_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id);


--
-- Name: auth_user_groups auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.auth_group(id);


--
-- Name: auth_user_groups auth_user_groups_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: deelflow_campaignrecipient deelflow_campaignrecipient_campaign_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_campaignrecipient
    ADD CONSTRAINT deelflow_campaignrecipient_campaign_id_fkey FOREIGN KEY (campaign_id) REFERENCES public.deelflow_outreachcampaign(id);


--
-- Name: deelflow_campaignrecipient deelflow_campaignrecipient_lead_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_campaignrecipient
    ADD CONSTRAINT deelflow_campaignrecipient_lead_id_fkey FOREIGN KEY (lead_id) REFERENCES public.deelflow_discoveredlead(id);


--
-- Name: deelflow_lead deelflow_lead_campaign_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_lead
    ADD CONSTRAINT deelflow_lead_campaign_id_fkey FOREIGN KEY (campaign_id) REFERENCES public.deelflow_campaign(id);


--
-- Name: deelflow_role_permissions deelflow_role_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_role_permissions
    ADD CONSTRAINT deelflow_role_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.deelflow_permission(id);


--
-- Name: deelflow_role_permissions deelflow_role_permissions_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_role_permissions
    ADD CONSTRAINT deelflow_role_permissions_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.deelflow_role(id);


--
-- Name: deelflow_user deelflow_user_organization_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deelflow_user
    ADD CONSTRAINT deelflow_user_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES public.deelflow_organization(id);


--
-- Name: django_admin_log django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id);


--
-- Name: django_admin_log django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- PostgreSQL database dump complete
--

\unrestrict IccbhRcVDUGdGKGQWH39DDOtbr5ePNAMuS4bZ3tIkm0a0ODMkZg350kcFE2WLEp

