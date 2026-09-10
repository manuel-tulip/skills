-- Pi evidence candidates; inspect returned results and corroborate git artifacts.
SELECT emitting_turn_index AS turn_index, tool_call_id, tool_name,
       file_path, success, exit_code,
       coalesce(nullif(command,''), json_extract(arguments_json,'$.command'), '') AS command_text,
       substr(result,1,16000) AS result_excerpt,
       arguments_json
FROM tool_calls
WHERE (tool_name='read' AND emitting_turn_index IN (4,1187,1188,1440))
   OR (tool_name='bash' AND emitting_turn_index>=1100
       AND (result LIKE '%new blank line at EOF%'
            OR arguments_json LIKE '%03-review-textbook.py%'
            OR arguments_json LIKE '%04-render-textbook.cjs%'))
ORDER BY emitting_turn_index;
