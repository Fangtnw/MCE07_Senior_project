// ***************************************************************************************************************************************************//      |              This script was auto-generated by generate_library.py which received parameters from setup_xicro.yaml                   |//      |                                         EDITING THIS FILE BY HAND IS NOT RECOMMENDED                                                 |// ***************************************************************************************************************************************************#ifndef XICRO_DIFFDRIVE_ID_10_H#define XICRO_DIFFDRIVE_ID_10_H

#include "Arduino.h" 
#define __UART_TYPE Stream
#define __STR_TYPE String

class Xicro{
    public:
        Xicro();
        void begin(__UART_TYPE *SerialObject);
        void Spin_node();void Test();
        // gen struct
        // gen public pub void        void publish_diff_imu_raw();
        void publish_diff_encoder_vel();
        // gen pub struct        struct{            struct{            float orientation_covariance[9]={0};            float angular_velocity_covariance[9]={0};            float linear_acceleration_covariance[9]={0};        struct{        struct{            int32_t sec= 0;            uint32_t nanosec= 0;        } stamp;            String frame_id= "";        } header;        struct{            float x= 0;            float y= 0;            float z= 0;            float w= 0;        } orientation;        struct{            float x= 0;            float y= 0;            float z= 0;        } angular_velocity;        struct{            float x= 0;            float y= 0;            float z= 0;        } linear_acceleration;            } message;         } Publisher_diff_imu_raw;        struct{            struct{        struct{        struct{            int32_t sec= 0;            uint32_t nanosec= 0;        } stamp;            String frame_id= "";        } header;        struct{            float x= 0;            float y= 0;            float z= 0;        } vector;            } message;         } Publisher_diff_encoder_vel;        // gen Sub struct        struct{            struct{        struct{            float x= 0;            float y= 0;            float z= 0;        } linear;        struct{            float x= 0;            float y= 0;            float z= 0;        } angular;            } message;         } Subscription_cmd_vel_follower;        // gen struct srv client         // gen service call void        // gen struct srv server        // gen void begin srv server        // gen service server response void        // gen action client call void        // gen struct action client         // gen struct action server         // gen void begin action server        // gen action server feedback void        // gen action server response void        




        struct{
            uint8_t server_not_response = 252;
            uint8_t server_return_none = 253;
            uint8_t get_response_done = 2;
            uint8_t client_request_done = 1;
            uint8_t initstate = 0;
        } service_client_state;

        

        struct{
            uint8_t client_request_done = 1;
            uint8_t goal_accept = 95;
            uint8_t goal_reject = 96;
            uint8_t incoming_feedback = 2;
            uint8_t get_result_done = 2;
            uint8_t server_return_none = 253;
            uint8_t initstate = 0;
            uint8_t server_not_response = 252;
            uint8_t time_out = 97;
        } action_client_state;
    // get    
    private:
        // gen id mcu
        uint8_t _Idmcu=10;
        __UART_TYPE* _serial;
        uint8_t _getcrc(uint8_t crc,uint8_t *data,uint16_t len);
        const uint8_t _CRC_8_TABLE[256] = {0x00,0x5E,0xBC,0xE2,0x61,0x3F,0xDD,0x83,0xC2,0x9C,0x7E,0x20,0xA3,0xFD,0x1F,0x41,0x9D,0xC3,0x21,0x7F,0xFC,0xA2,0x40,0x1E,0x5F,0x01,0xE3,0xBD,0x3E,0x60,0x82,0xDC,0x23,0x7D,0x9F,0xC1,0x42,0x1C,0xFE,0xA0,0xE1,0xBF,0x5D,0x03,0x80,0xDE,0x3C,0x62,0xBE,0xE0,0x02,0x5C,0xDF,0x81,0x63,0x3D,0x7C,0x22,0xC0,0x9E,0x1D,0x43,0xA1,0xFF,0x46,0x18,0xFA,0xA4,0x27,0x79,0x9B,0xC5,0x84,0xDA,0x38,0x66,0xE5,0xBB,0x59,0x07,0xDB,0x85,0x67,0x39,0xBA,0xE4,0x06,0x58,0x19,0x47,0xA5,0xFB,0x78,0x26,0xC4,0x9A,0x65,0x3B,0xD9,0x87,0x04,0x5A,0xB8,0xE6,0xA7,0xF9,0x1B,0x45,0xC6,0x98,0x7A,0x24,0xF8,0xA6,0x44,0x1A,0x99,0xC7,0x25,0x7B,0x3A,0x64,0x86,0xD8,0x5B,0x05,0xE7,0xB9,0x8C,0xD2,0x30,0x6E,0xED,0xB3,0x51,0x0F,0x4E,0x10,0xF2,0xAC,0x2F,0x71,0x93,0xCD,0x11,0x4F,0xAD,0xF3,0x70,0x2E,0xCC,0x92,0xD3,0x8D,0x6F,0x31,0xB2,0xEC,0x0E,0x50,0xAF,0xF1,0x13,0x4D,0xCE,0x90,0x72,0x2C,0x6D,0x33,0xD1,0x8F,0x0C,0x52,0xB0,0xEE,0x32,0x6C,0x8E,0xD0,0x53,0x0D,0xEF,0xB1,0xF0,0xAE,0x4C,0x12,0x91,0xCF,0x2D,0x73,0xCA,0x94,0x76,0x28,0xAB,0xF5,0x17,0x49,0x08,0x56,0xB4,0xEA,0x69,0x37,0xD5,0x8B,0x57,0x09,0xEB,0xB5,0x36,0x68,0x8A,0xD4,0x95,0xCB,0x29,0x77,0xF4,0xAA,0x48,0x16,0xE9,0xB7,0x55,0x0B,0x88,0xD6,0x34,0x6A,0x2B,0x75,0x97,0xC9,0x4A,0x14,0xF6,0xA8,0x74,0x2A,0xC8,0x96,0x15,0x4B,0xA9,0xF7,0xB6,0xE8,0x0A,0x54,0xD7,0x89,0x6B,0x35};
        uint8_t _start[4]={73,109,64,99};
        uint8_t _stop[2]={126,126};
        uint8_t _continue[2]={42,42};
        void _Sendstart();
        void _SendSignature(uint8_t Idmcu,uint8_t Mode);
        void _Sendstop();
        void _Sendcontinue();
        void _SendUint8(uint8_t *data,uint8_t len);
        void _SendUint16(uint16_t *data,uint8_t len);
        void _SendUint32(uint32_t *data,uint8_t len);
        void _SendUint64(uint64_t *data,uint8_t len);
        void _SendInt8(int8_t *data,uint8_t len);
        void _SendInt16(int16_t *data,uint8_t len);
        void _SendInt32(int32_t *data,uint8_t len);
        void _SendInt64(int64_t *data,uint8_t len);
        void _SendFloat32(float *data,uint8_t len);
        void _SendString(__STR_TYPE *data,uint8_t len);
        void _SendBool(bool *data,uint8_t len,bool flagNext);
        void _SendIdTopic(uint8_t IdTopic);
        void _SendEmpty();

        uint8_t _crc=0;
        void _Sendcrc();
        uint8_t _state=0;
        uint8_t _datain[1]={0};
        uint64_t _bb=0;
        
        
        uint8_t _incomingIndexTopic=0;
        int8_t _OnTopic=-1;
        uint8_t _Ontype=0;
        uint8_t _Indexdata=0;
        uint8_t _crcIn=0;
       

        __STR_TYPE _bufff="";
        uint8_t q=0;
        uint8_t w=0; 
        uint8_t _loop=0;
        uint8_t _loopTo=0;
        // gen private struct
        // gen Sub        void* _nonverify[1][6][1];        void* _verify[1][6][1];        uint8_t _Idtopic_sub[1]={1};        uint8_t _TopicType[1][6]={{111,111,111,111,111,111}};        uint8_t _Totalvar[1]={6};        uint8_t _Nofdata[1][6]={{1, 1, 1, 1, 1, 1}};        // gen client res        void* _nonverify_srv_client_res[0][0][0];        void* _verify_srv_client_res[0][0][0];        uint8_t _Idsrv_client[0]={};        uint8_t _Srv_client_res_Type[0][0]={};        uint8_t _Totalvar_srv_client_res[0]={};        uint8_t _Nofdata_srv_client_res[0][0]={};        void* _nonverify_srv_client_state[0];        void* _verify_srv_client_state[0];        // gen server req        void* _nonverify_srv_server_req[0][0][0];        void* _verify_srv_server_req[0][0][0];        uint8_t _Idsrv_server[0]={};        uint8_t _Srv_server_req_Type[0][0]={};        uint8_t _Totalvar_srv_server_req[0]={};        uint8_t _Nofdata_srv_server_req[0][0]={};        void* _nonverify_srv_server_state[0];        void* _verify_srv_server_state[0];        // gen private struct sub        struct{            struct{        struct{            float x= 0;            float y= 0;            float z= 0;        } linear;        struct{            float x= 0;            float y= 0;            float z= 0;        } angular;            } message;         }_Subscription_cmd_vel_follower;        // gen private struct srv        // gen private struct srv        // gen private struct action        // gen private struct action        // gen pointer srv server void        void* _service_server[0];        // gen action client feed res        void* _nonverify_action_client_res[0][0][0];        void* _verify_action_client_res[0][0][0];        uint8_t _Idaction_client[0]={};        uint8_t _Action_client_res_Type[0][0]={};        uint8_t _Totalvar_action_client_res[0]={};        uint8_t _Nofdata_action_client_res[0][0]={};        void* _nonverify_action_client_feed[0][0][0];        void* _verify_action_client_feed[0][0][0];        uint8_t _Action_client_feed_Type[0][0]={};        uint8_t _Totalvar_action_client_feed[0]={};        uint8_t _Nofdata_action_client_feed[0][0]={};        void* _nonverify_action_client_state[0];        void* _verify_action_client_state[0];        // gen pointer srv server void        void* _action_server[0];        // gen action server goal        void* _nonverify_action_server_req[0][0][0];        void* _verify_action_server_req[0][0][0];        uint8_t _Idaction_server[0]={};        uint8_t _Action_server_req_Type[0][0]={};        uint8_t _Totalvar_action_server_req[0]={};        uint8_t _Nofdata_action_server_req[0][0]={};        void* _nonverify_action_server_state[0];        void* _verify_action_server_state[0];



        uint8_t _Onindex=0;
        uint8_t _Ongrab=0;
        uint8_t _OngrabTo=0;
        uint8_t _statetogo=0;
        uint8_t _OnMode=0;


};
#endif